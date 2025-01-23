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
			const response = await getSearch({ query: { query: q } });
			if (response.data) {
				this.results = response.data;
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
			const response = await getNextSearch();
			if (response.data) {
				this.results = [...this.results, ...response.data];
			}
			toasts.success('Success', `Found ${this.results.length} more search results.`);
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
