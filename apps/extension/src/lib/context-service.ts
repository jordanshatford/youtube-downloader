import { defineProxyService } from '@webext-core/proxy-service';
import { get } from 'svelte/store';
import { Tabs } from 'webextension-polyfill';

import {
	client,
	deleteDownload,
	Download,
	DownloadOptions,
	getDownloadFile,
	getDownloadsStatus,
	getSession,
	getSessionValidate,
	getVideo,
	postDownloads,
	putDownloads,
	Session,
	Video
} from '@yd/client';

import { env } from '~/lib/config';
import { setContextMenus } from '~/lib/context-menu';
import { isYouTubeVideo } from '~/lib/detect';
import { saveAs } from '~/lib/files';
import { sendMessageIgnoreReturn } from '~/lib/messaging';
import { settings } from '~/lib/stores/settings';

export type Ctx = {
	session?: Session; // Current session.
	video?: Video; // YouTube video in current tab.
	options: DownloadOptions; // Preferred download options.
	downloads: Record<string, Download>; // Map of downloads.
};

// Duration to wait (ms) before re-attempting to setup a session.
const REATTEMPT_INTERVAL = 10000;

// Awaitable function to sleep for some duration. Used when re-attempting to setup
// the users session.
const sleep = (ms: number) => new Promise((resolve) => setTimeout(resolve, ms));

// Key used to store session ID value in session storage.
const SESSION_ID_KEY = 'yd-sessionid';

// Set the base server address using the environment variable.
client.setConfig({
	baseUrl: env.serverAddress,
	throwOnError: true
});

async function getSessionIdFromStorage() {
	const result = await browser.storage.sync.get(SESSION_ID_KEY);
	const token = result?.[SESSION_ID_KEY] ?? '';
	return token;
}

// Use session as token when making requests with client. Take this
// token from the session storage, as it is set there on session setup.
client.interceptors.request.use(async (request) => {
	const token = await getSessionIdFromStorage();
	request.headers.set('Authorization', `Bearer ${token}`);
	return request;
});

class ContextService {
	// Current session and eventsource being used.
	#session?: Session;
	#eventSource?: EventSource;

	// Current tab and video context.
	#currentTab?: Tabs.Tab;
	#tabVideos: Record<string, Video | undefined> = {};

	#loading: boolean = false;

	// Video cache of previous search results.
	#videoCache: Record<string, Video> = {};

	// Map of downloads.
	#downloads: Record<string, Download> = {};

	/**
	 * Set current context based on a browser tab.
	 * @param tab Tabs.Tab - the browser Tab
	 */
	public async setTab(tab: Tabs.Tab): Promise<void> {
		this.#loading = true;
		const currentTab = this.#currentTab;
		this.#currentTab = tab;

		// Ignore tab if it matches the current context. Keep video the same.
		if (!tab.url || tab.url === currentTab?.url) {
			this.#loading = false;
			return;
		}

		// Ignore the tab if it is not a YouTube video. We also set the current video
		// to undefined so previous tab video isnt persisted.
		if (!tab.url || !isYouTubeVideo(tab.url)) {
			if (this.#tabVideos[tab.url] !== undefined) {
				this.#tabVideos[tab.url] = undefined;
				await setContextMenus(undefined);
				await sendMessageIgnoreReturn('VideoChanged', { tab, video: undefined });
			}
			this.#loading = false;
			return;
		}

		// Ensure session exists for the user.
		await this.#ensureSession();

		// Get the video of the current tab.
		const url = new URL(tab.url);
		const id = url.searchParams.get('v')!;

		// Check if video is cached.
		if (this.#videoCache[id]) {
			this.#tabVideos[tab.url] = this.#videoCache[id];
			await setContextMenus(this.#videoCache[id]);
			await sendMessageIgnoreReturn('VideoChanged', { tab, video: this.#videoCache[id] });
			this.#loading = false;
			return;
		}

		// Fetch the video from the API and cache it.
		try {
			const response = await getVideo({ query: { id } });
			if (response.data) {
				const video = response.data;
				this.#tabVideos[tab.url] = video;
				this.#videoCache[id] = video;
				await setContextMenus(video);
				await sendMessageIgnoreReturn('VideoChanged', { tab, video });
			}
			this.#loading = false;
			return;
		} catch {
			this.#loading = false;
			return;
		}
	}

	/**
	 * Get the context of the current tab.
	 * @returns Ctx - the context of the tab.
	 */
	public async get(): Promise<Ctx> {
		// Ensure we arent waiting for a video
		while (this.#loading) {
			await sleep(100);
		}
		// Get current tab to ensure we are showing correct video.
		const [tab] = await browser.tabs.query({ active: true, currentWindow: true });
		// Ensure settings are initialized with browser storage settings.
		await settings.initialize();
		return {
			video: tab.url ? this.#tabVideos[tab.url] : undefined,
			session: this.#session,
			options: get(settings),
			downloads: this.#downloads
		};
	}

	/**
	 * Download the video currently in context.
	 */
	public async download(video: Video): Promise<void> {
		// Ensure we have a session.
		await this.#ensureSession();

		// Make download based on current video.
		const download: Download = {
			video,
			options: get(settings),
			status: {
				state: 'WAITING',
				progress: null
			}
		};

		// Store downloads in map.
		this.#downloads[video.id] = download;

		// Send the download to the API.
		await postDownloads({ body: download });
		await sendMessageIgnoreReturn('DownloadStart', download);
	}

	public async downloadURL(url: string): Promise<void> {
		// Get video from URL.
		const id = new URL(url).searchParams.get('v')!;
		const video = this.#videoCache[id];
		// If download already present ignore it.
		if (video.id in this.#downloads) {
			return;
		}
		await this.download(video);
	}

	public async getFile(id: string): Promise<void> {
		if (!(id in this.#downloads)) return;

		const response = await getDownloadFile({ path: { download_id: id } });
		if (response.data) {
			const download = this.#downloads[id];
			const filename = `${download.video.title}.${download.options.format}`;

			try {
				await saveAs(response.data, filename);
			} catch (e) {
				console.error(`Failed to save download file for ${download.video.title}: `, e);
			}
		}
	}

	public async remove(id: string): Promise<void> {
		if (!(id in this.#downloads)) return;
		await this.#ensureSession();
		await deleteDownload({ path: { download_id: id } });
		delete this.#downloads[id];
		sendMessageIgnoreReturn('DownloadRemove', id);
	}

	public async restart(id: string): Promise<void> {
		if (!(id in this.#downloads)) return;
		const download = this.#downloads[id];
		const result = await putDownloads({ body: download });
		if (result.data) {
			this.#downloads[download.video.id] = result.data;
			await sendMessageIgnoreReturn('StatusUpdate', result.data);
		}
	}

	/**
	 * Ensure that the user has a session that is valid. This updates the private session variable.
	 */
	async #ensureSession(): Promise<void> {
		try {
			// Attempt to use existing session if present.
			const response = await getSessionValidate();
			if (response.data) {
				await browser.storage.sync.set({ [SESSION_ID_KEY]: response.data?.id });
				this.#session = response.data;
			}
		} catch {
			// Attempt to setup a new session until successful
			let session: Session | undefined;
			while (session === undefined) {
				try {
					// Attempt to setup new session.
					session = (await getSession()).data;
					if (session) {
						await browser.storage.sync.set({ [SESSION_ID_KEY]: session?.id });
						this.#session = session;
						await sendMessageIgnoreReturn('NewSession', this.#session);
					}
				} catch (err) {
					console.error('Connection failed, could not connect to internal server. ', err);
					await sleep(REATTEMPT_INTERVAL);
				}
			}
		}
		// Create event source if one does not exist.
		if (!this.#eventSource) {
			this.#eventSource = await getDownloadsStatus(getSessionIdFromStorage, {
				onMessage: async (value) => {
					this.#downloads[value.video.id] = value;
					await sendMessageIgnoreReturn('StatusUpdate', value);
					// If download is DONE, get the file and save to users computer.
					if (value.status.state === 'DONE') {
						await sendMessageIgnoreReturn('DownloadDone', value);
						await this.getFile(value.video.id);
					}
				}
			});
		}
	}
}

export const [registerContextService, getContextService] = defineProxyService(
	'ContextService',
	() => new ContextService()
);
