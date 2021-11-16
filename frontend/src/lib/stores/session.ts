import { browser } from '$app/env'
import { writable } from 'svelte/store'
import { getApiEndpoint } from '$lib/utils/functions'
import { notifications } from '$lib/stores/notifications'

function createSessionStore() {
	const API_ENDPOINT = '/session'
	const RE_ATTEMPT_INTERVAL = 10000

	const { subscribe, set } = writable(null)

	async function setup() {
		const url = getApiEndpoint(API_ENDPOINT)
		if (browser) {
			await fetch(url, { credentials: 'include' })
				.then(() => {
					set('session-set')
				})
				.catch((err) => {
					console.error('Connection failed, could not connect to internal server. ', err)
					notifications.warning(
						'Connection Failed',
						'Could not connect to internal server. Retrying in 10 seconds.'
					)
					_reAttempt()
				})
		}
	}

	async function _reAttempt() {
		setTimeout(() => {
			setup()
		}, RE_ATTEMPT_INTERVAL)
	}

	return {
		subscribe,
		setup,
		reset: () => set(null)
	}
}

export const session = createSessionStore()
