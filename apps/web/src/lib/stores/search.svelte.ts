import type { SearchState } from '@yd/client';
import { getSearch, getSearchNext, getSearchState } from '@yd/client';
import { toast } from '@yd/ui';

class SearchStore {
	public state = $state<SearchState>({ query: '', results: [] });
	public loading = $state<boolean>(false);

	public async init() {
		// Get existing search state to prevent search page from clearing on page reload.
		try {
			const { data: state } = await getSearchState();
			if (state) {
				this.state = state;
			}
		} catch (e) {
			console.error('Failed to get initial search state ', e);
			return;
		}
	}

	public async get(q: string) {
		if (this.state.query === q) {
			return;
		}
		this.state = { query: q, results: [] };
		this.loading = true;
		toast.promise(getSearch({ query: { query: q } }), {
			loading: 'Searching...',
			success: ({ data: results }) => {
				if (results) {
					this.state.results = results;
				}
				return `Found ${results?.length} search results.`;
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
		toast.promise(getSearchNext(), {
			loading: 'Searching...',
			success: ({ data: results }) => {
				if (results) {
					this.state.results = [...(this.state?.results ?? []), ...results];
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
		this.state = { query: '', results: [] };
		this.loading = false;
	}
}

export const search = new SearchStore();
