import { writable } from 'svelte/store'
import type { VideoInfo } from '$lib/utils/types'
import { getApiEndpoint, APIEndpointConstants } from '$lib/utils/api'

function createSearchStore() {
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
		const { endpoint, options } = getApiEndpoint({
			base: APIEndpointConstants.SEARCH,
			method: 'GET',
			queryParams: {
				term: term
			}
		})
		fetch(endpoint, options)
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
