import { writable } from 'svelte/store';

import type { Video } from '@yd/client';
import { getNextSearch, getSearch } from '@yd/client';
import { toasts } from '@yd/ui';

function createSearchStore() {
	const results: Video[] = [];

	const { subscribe, set, update } = writable({
		query: '',
		results: results,
		loading: false
	});

	async function get(query: string) {
		let hasSearchChanged = false;
		update((state) => {
			if (state.query === query) {
				return state;
			}
			hasSearchChanged = true;
			state.query = query;
			state.loading = true;
			return state;
		});
		if (hasSearchChanged) {
			let results: Video[] = [];
			try {
				const response = await getSearch({ query: { query } });
				if (response.data) {
					results = response.data;
				}
				toasts.success('Success', `Found ${results.length} search results.`);
			} catch (err) {
				toasts.error('Error', 'Failed to get search results.');
				console.error('Failed to search for videos ', err);
			}
			update((state) => {
				state.results = results;
				state.loading = false;
				return state;
			});
		}
	}

	async function getMore() {
		update((state) => {
			state.loading = true;
			return state;
		});
		let results: Video[] = [];
		try {
			const response = await getNextSearch();
			if (response.data) {
				results = response.data;
			}
			toasts.success('Success', `Found ${results.length} more search results.`);
		} catch (err) {
			toasts.error('Error', 'Failed to get more search results.');
			console.error('Failed to get more search videos ', err);
		}
		update((state) => {
			state.results = [...state.results, ...results];
			state.loading = false;
			return state;
		});
	}

	return {
		subscribe,
		get,
		getMore,
		reset: () => set({ query: '', results: [], loading: false })
	};
}

export const search = createSearchStore();
