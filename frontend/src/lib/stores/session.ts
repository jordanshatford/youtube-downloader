import { writable } from 'svelte/store'
import { getApiEndpoint, APIEndpointConstants } from '$lib/utils/APIUtils'
import { notifications } from '$lib/stores/notifications'

function createSessionStore() {
	const RE_ATTEMPT_INTERVAL = 10000

	const { subscribe, set } = writable(null)

	async function setup() {
		const url = getApiEndpoint(APIEndpointConstants.SESSION)
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
