import { OpenAPI, SessionService } from '@yd/client';
import { toast } from '@yd/ui';
import { env } from '$lib/config';
import { browser } from '$app/environment';

// Set the base server address using the environment variable.
OpenAPI.BASE = env.serverAddress;

// Use session as token when making requests with client. Take this
// token from the session storage, as it is set there on session setup.
OpenAPI.TOKEN = async () => {
	return sessionStorage.getItem(SESSION_ID_KEY) ?? '';
};

// Key used to store session ID value in session storage.
const SESSION_ID_KEY = 'sessionId';

// Duration to wait (ms) before re-attempting to setup a session.
const REATTEMPT_INTERVAL = 10000;

// Function used to setup a users session with a callback when it is successful.
// This will re-attempt to setup a session until successful.
export async function setupSession(onSuccess?: () => void) {
	if (browser) {
		// await session.setup();
		console.log(SESSION_ID_KEY);
		try {
			// Attempt to use existing session if present.
			const session = await SessionService.getSessionValidate();
			sessionStorage.setItem(SESSION_ID_KEY, session.id);
		} catch (err) {
			// Attempt to setup a new session until successful
			let success = false;
			while (!success) {
				try {
					// Attempt to setup new session.
					const session = await SessionService.getSession();
					sessionStorage.setItem(SESSION_ID_KEY, session.id);
					success = true;
				} catch (err) {
					toast.error('Error', 'Failed to setup session. Re-attempting shortly.');
					console.error('Connection failed, could not connect to internal server. ', err);
					await sleep(REATTEMPT_INTERVAL);
				}
			}
		}
		onSuccess?.();
	}
}

// Awaitable function to sleep for some duration. Used when re-attempting to setup
// the users session.
const sleep = (ms: number) => new Promise((resolve) => setTimeout(resolve, ms));
