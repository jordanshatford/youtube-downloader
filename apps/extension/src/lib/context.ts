import { get } from 'svelte/store';
import { Tabs } from 'webextension-polyfill';
import {
	OpenAPI,
	SessionService,
	SearchService,
	type Video,
	type Session,
	type DownloadOptions
} from '@yd/client';
import { isYouTubeVideo } from '~/lib/detect';
import { env } from '~/lib/config';
import { settings } from '~/lib/stores/settings';

// Key used to store session ID value in session storage.
const SESSION_ID_KEY = 'sessionId';

// Duration to wait (ms) before re-attempting to setup a session.
const REATTEMPT_INTERVAL = 10000;

// Set the base server address using the environment variable.
OpenAPI.BASE = env.serverAddress;

// Use session as token when making requests with client. Take this
// token from the session storage, as it is set there on session setup.
OpenAPI.TOKEN = async () => {
	const result = await browser.storage.sync.get(SESSION_ID_KEY);
	return result?.[SESSION_ID_KEY] ?? '';
};

// Setup session using current user session or re-attempt until new session
// is created.
export async function setupSession(): Promise<Session> {
	try {
		// Attempt to use existing session if present.
		const session = await SessionService.getSessionValidate();
		return session;
	} catch (err) {
		// Attempt to setup a new session until successful
		let session: Session | undefined;
		while (session === undefined) {
			try {
				// Attempt to setup new session.
				session = await SessionService.getSession();
				return session;
			} catch (err) {
				console.error('Connection failed, could not connect to internal server. ', err);
				await sleep(REATTEMPT_INTERVAL);
			}
		}
		throw Error('Could not setup session.');
	}
}

// Awaitable function to sleep for some duration. Used when re-attempting to setup
// the users session.
const sleep = (ms: number) => new Promise((resolve) => setTimeout(resolve, ms));

export type Ctx = {
	tab: Tabs.Tab; // The current tab.
	video?: Video; // YouTube video in current tab.
	session?: Session; // Current session.
	options: DownloadOptions; // Preferred download options.
};

// Function used to ensure current context for the extension (ie session setup, current tab, and video if possibe )
export async function setupContext(): Promise<Ctx> {
	// Check that the current tab is for a YouTube video, if not ignore.
	const tabs = await browser.tabs.query({ active: true, currentWindow: true });
	const tab = tabs[0];
	if (!tab.url || !isYouTubeVideo(tab.url)) {
		throw Error('Ignoring page that is not a YouTube video.');
	}

	// Setup and store session for current use.
	const session = await setupSession();
	await browser.storage.sync.set({ [SESSION_ID_KEY]: session.id });

	// Get the vidoe of the current tab.
	const url = new URL(tab.url);
	const id = url.searchParams.get('v')!;
	const video = await SearchService.getVideo(id);

	// Get prefered options based on user settings.
	await settings.initialize();
	const options = get(settings);

	// Return relevant context to be used in the extension.
	return {
		tab,
		session,
		video,
		options
	};
}
