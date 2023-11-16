import { get } from 'svelte/store';
import { defineProxyService } from '@webext-core/proxy-service';
import { Tabs } from 'webextension-polyfill';
import {
	OpenAPI,
	Video,
	Download,
	Session,
	DownloadOptions,
	SessionService,
	SearchService,
	DownloadState,
	DownloadsService,
	DownloadsStatusService
} from '@yd/client';
import { settings } from '~/lib/stores/settings';
import { env } from '~/lib/config';
import { isYouTubeVideo } from '~/lib/detect';
import { sendMessageIgnoreReturn } from '~/lib/messaging';
import { saveAs } from '~/lib/files';

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
const SESSION_ID_KEY = 'sessionId';

// Set the base server address using the environment variable.
OpenAPI.BASE = env.serverAddress;

// Use session as token when making requests with client. Take this
// token from the session storage, as it is set there on session setup.
OpenAPI.TOKEN = async () => {
	const result = await browser.storage.sync.get(SESSION_ID_KEY);
	return result?.[SESSION_ID_KEY] ?? '';
};

class ContextService {
	// Current session and eventsource being used.
	#session?: Session;
	#eventSource?: EventSource;

	// Current tab and video context.
	#currentTab?: Tabs.Tab;
	#currentTabVideo?: Video;

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
			if (this.#currentTabVideo !== undefined) {
				this.#currentTabVideo = undefined;
				await sendMessageIgnoreReturn('VideoChanged', this.#currentTabVideo);
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
			this.#currentTabVideo = this.#videoCache[id];
			await sendMessageIgnoreReturn('VideoChanged', this.#currentTabVideo);
			this.#loading = false;
			return;
		}

		// Fetch the video from the API and cache it.
		try {
			const video = await SearchService.getVideo(id);
			this.#currentTabVideo = video;
			this.#videoCache[id] = video;
			await sendMessageIgnoreReturn('VideoChanged', this.#currentTabVideo);
			this.#loading = false;
			return;
		} catch (e) {
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

		// If video is undefined we dont have valid context.
		if (!this.#currentTabVideo) {
			throw Error('Page does not contain a valid YouTube video.');
		}
		// Ensure settings are initialized with browser storage settings.
		await settings.initialize();
		return {
			video: this.#currentTabVideo,
			session: this.#session,
			options: get(settings),
			downloads: this.#downloads
		};
	}

	/**
	 * Download the video currently in context.
	 */
	public async download(): Promise<void> {
		// If there is no video, ignore.
		if (!this.#currentTabVideo) {
			return;
		}

		// Ensure we have a session.
		await this.#ensureSession();

		// Make download based on current video.
		const download = {
			video: this.#currentTabVideo,
			options: get(settings),
			status: {
				state: DownloadState.WAITING,
				progress: null
			}
		};

		// Store downloads in map.
		this.#downloads[this.#currentTabVideo.id] = download;

		// Send the download to the API.
		await DownloadsService.postDownloads(download);
		await sendMessageIgnoreReturn('DownloadStart', download);
	}

	/**
	 * Ensure that the user has a session that is valid. This updates the private session variable.
	 */
	async #ensureSession(): Promise<void> {
		try {
			// Attempt to use existing session if present.
			const session = await SessionService.getSessionValidate();
			await browser.storage.sync.set({ [SESSION_ID_KEY]: session?.id });
			this.#session = session;
		} catch (err) {
			// Attempt to setup a new session until successful
			let session: Session | undefined;
			while (session === undefined) {
				try {
					// Attempt to setup new session.
					session = await SessionService.getSession();
					await browser.storage.sync.set({ [SESSION_ID_KEY]: session?.id });
					this.#session = session;
					await sendMessageIgnoreReturn('NewSession', this.#session);
				} catch (err) {
					console.error('Connection failed, could not connect to internal server. ', err);
					await sleep(REATTEMPT_INTERVAL);
				}
			}
		}
		// Create event source if one does not exist.
		if (!this.#eventSource) {
			this.#eventSource = await DownloadsStatusService.setup(async (value) => {
				this.#downloads[value.video.id] = value;
				await sendMessageIgnoreReturn('StatusUpdate', value);
				// If download is DONE, get the file and save to users computer.
				if (value.status.state === DownloadState.DONE) {
					const blob = await DownloadsService.getDownloadFile(value.video.id);
					const filename = `${value.video.title} - ${value.video.channel.name}.${value.options.format}`;
					try {
						await saveAs(blob, filename);
						await sendMessageIgnoreReturn('DownloadDone', value);
					} catch (e) {
						console.error(`Failed to save download file for ${value.video.title}: `, e);
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
