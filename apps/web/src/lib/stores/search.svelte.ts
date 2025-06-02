import type { Video } from '@yd/client';
import { getNextSearch, getSearch } from '@yd/client';
import { toasts } from '@yd/ui';

class SearchStore {
	public query = $state<string>('');
	public loading = $state<boolean>(false);
	public results = $state<Video[]>([]);

	public async get(q: string) {
		if (this.query === q) {
			return;
		}
		this.query = q;
		this.loading = true;
		try {
			const { data: results } = await getSearch({ query: { query: q } });
			if (results) {
				this.results = results;
			}
			toasts.success('Success', `Found ${this.results.length} search results.`);
		} catch (err) {
			toasts.error('Error', 'Failed to get search results.');
			console.error('Failed to search for videos ', err);
		}
		this.loading = false;
	}

	public async getMore() {
		this.loading = true;
		try {
			const { data: results } = await getNextSearch();
			if (results) {
				this.results = [...this.results, ...results];
				toasts.success('Success', `Found ${results?.length} more search results.`);
			}
		} catch (err) {
			toasts.error('Error', 'Failed to get more search results.');
			console.error('Failed to get more search videos ', err);
		}
		this.loading = false;
	}

	public reset() {
		this.query = '';
		this.loading = false;
		this.results = [];
	}
}

export const search = new SearchStore();
