import { writable } from 'svelte/store'
import type { VideoInfo } from '$lib/utils/types'
import { getApiEndpoint, APIEndpointConstants } from '$lib/utils/APIUtils'

function createSearchStore() {
	const DEFAULT_NUMBER_OF_RESULTS = 12
	const results: VideoInfo[] = []

	const { subscribe, set, update } = writable({
		term: '',
		results: results,
		loading: false
	})

	function get(term: string) {
		update((state) => {
			state.term = term
			state.loading = true
			return state
		})
		const { endpoint } = getApiEndpoint({
			base: APIEndpointConstants.SEARCH,
			queryParams: {
				term: term,
				results: DEFAULT_NUMBER_OF_RESULTS
			}
		})
		fetch(endpoint, { method: 'GET', credentials: 'include', headers: { 'x-session-id': 'test' } })
			.then((response) => response.json())
			.then((results) => {
				update((state) => {
					state.results = results
					state.loading = false
					return state
				})
			})
	}

	return {
		subscribe,
		get,
		reset: () => set({ term: '', results: [], loading: false })
	}
}

export const search = createSearchStore()
