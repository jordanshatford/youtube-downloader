import { writable } from 'svelte/store';
import { SearchService, type Video } from '@yad/client';

function createSearchStore() {
	const results: Video[] = [];

	const { subscribe, set, update } = writable({
		term: '',
		results: results,
		loading: false
	});

	async function get(term: string) {
		update((state) => {
			state.term = term;
			state.loading = true;
			return state;
		});
		const results = await SearchService.getSearch(term);
		update((state) => {
			state.results = results;
			state.loading = false;
			return state;
		});
	}

	return {
		subscribe,
		get,
		reset: () => set({ term: '', results: [], loading: false })
	};
}

export const search = createSearchStore();
