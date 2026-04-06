import type { Video } from '@yd/client';
import { getNextSearch, getSearch } from '@yd/client';
import { toast } from '@yd/ui';

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
		toast.promise(getSearch({ query: { query: q } }), {
			loading: 'Searching...',
			success: ({ data: results }) => {
				if (results) {
					this.results = results;
				}
				return `Found ${this.results.length} search results.`;
			},
			error: (err) => {
				console.error('Failed to search for videos ', err);
				return 'Failed to get search results.';
			},
			finally: () => {
				this.loading = false;
			}
		});
	}

	public async getMore() {
		this.loading = true;
		toast.promise(getNextSearch(), {
			loading: 'Searching...',
			success: ({ data: results }) => {
				if (results) {
					this.results = [...this.results, ...results];
				}
				return `Found ${results?.length} more search results.`;
			},
			error: (err) => {
				console.error('Failed to get more search videos ', err);
				return 'Failed to get more search results.';
			},
			finally: () => {
				this.loading = false;
			}
		});
	}

	public reset() {
		this.query = '';
		this.loading = false;
		this.results = [];
	}
}

export const search = new SearchStore();
