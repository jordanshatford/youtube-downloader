import { writable } from 'svelte/store';
import { SearchService, type Video } from '@yd/client';
import { toast } from '$lib/components/ui/toast';

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
		let results: Video[] = [];
		try {
			results = await SearchService.getSearch(term);
			toast.success(`Found ${results.length} search results.`);
		} catch (err) {
			toast.error('Failed to get search results.');
			console.error('Failed to search for videos ', err);
		}
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
