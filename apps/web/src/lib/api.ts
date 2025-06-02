import { browser } from '$app/environment';
import { env } from '$lib/config';
import { downloads } from '$lib/stores/downloads.svelte';

import { client, getSession, getSessionValidate } from '@yd/client';
import { toasts } from '@yd/ui';

// Set the base server address using the environment variable.
client.setConfig({
	baseUrl: env.serverAddress,
	throwOnError: true,
	auth: () => localStorage.getItem(SESSION_ID_KEY)?.toString()
});

// Key used to store session ID value in session storage.
export const SESSION_ID_KEY = 'yd-sessionid';

// Duration to wait (ms) before re-attempting to setup a session.
const REATTEMPT_INTERVAL = 10000;

// Function used to setup a users session with a callback when it is successful.
// This will re-attempt to setup a session until successful. Once the session is ready
// downloads will be fetched and status event source will be created.
export async function setupSession(): Promise<void> {
	if (browser) {
		try {
			// Attempt to use existing session if present.
			const { data: session } = await getSessionValidate();
			if (session) {
				localStorage.setItem(SESSION_ID_KEY, session.id);
			}
		} catch {
			// Attempt to setup a new session until successful
			let success = false;
			while (!success) {
				try {
					// Attempt to setup new session.
					const { data: session } = await getSession();
					if (session) {
						localStorage.setItem(SESSION_ID_KEY, session.id);
						success = true;
					}
				} catch (err) {
					toasts.error('Error', 'Failed to setup session. Re-attempting shortly.');
					console.error('Connection failed, could not connect to internal server. ', err);
					await sleep(REATTEMPT_INTERVAL);
				}
			}
		}
		await downloads.init();
	}
}

// Awaitable function to sleep for some duration. Used when re-attempting to setup
// the users session.
const sleep = (ms: number) => new Promise((resolve) => setTimeout(resolve, ms));
