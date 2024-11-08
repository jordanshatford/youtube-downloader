import { browser } from '$app/environment';
import { env } from '$lib/config';
import { downloads } from '$lib/stores/downloads';

import { client, getSession, getSessionValidate } from '@yd/client';
import { toast } from '@yd/ui';

// Set the base server address using the environment variable.
client.setConfig({
	baseUrl: env.serverAddress,
	throwOnError: true
});

client.interceptors.request.use((request) => {
	const token = sessionStorage.getItem(SESSION_ID_KEY) ?? '';
	request.headers.set('Authorization', `Bearer ${token}`);
	return request;
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
			const session = await getSessionValidate();
			if (session.data) {
				sessionStorage.setItem(SESSION_ID_KEY, session.data.id);
			}
		} catch {
			// Attempt to setup a new session until successful
			let success = false;
			while (!success) {
				try {
					// Attempt to setup new session.
					const session = await getSession();
					sessionStorage.setItem(SESSION_ID_KEY, session.data?.id ?? '');
					success = true;
				} catch (err) {
					toast.error('Error', 'Failed to setup session. Re-attempting shortly.');
					console.error('Connection failed, could not connect to internal server. ', err);
					await sleep(REATTEMPT_INTERVAL);
				}
			}
		}
		downloads.setupStatusListener();
		await downloads.init();
	}
}

// Awaitable function to sleep for some duration. Used when re-attempting to setup
// the users session.
const sleep = (ms: number) => new Promise((resolve) => setTimeout(resolve, ms));
