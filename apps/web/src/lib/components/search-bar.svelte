<script lang="ts">
	import { InputGroup, SearchIcon, SpinnerIcon } from '@yd/ui';

	interface Props {
		loading?: boolean;
		query?: string;
		onsearch: (query: string) => void | Promise<void>;
	}

	let { loading = false, query = $bindable(), onsearch }: Props = $props();

	function onKeypressSearch(event: KeyboardEvent) {
		if (event.key === 'Enter' && query && query.length > 0) {
			onSearch();
		}
	}

	function onSearch() {
		if (query && query.length > 0) {
			onsearch(query);
		}
	}
</script>

<InputGroup.Root>
	<InputGroup.Input
		placeholder="Search..."
		bind:value={query}
		disabled={loading}
		onkeypress={onKeypressSearch}
		type="search"
	/>
	<InputGroup.Addon>
		{#if loading}
			<SpinnerIcon />
		{:else}
			<SearchIcon />
		{/if}
	</InputGroup.Addon>
	<InputGroup.Addon align="inline-end">
		<InputGroup.Button variant="secondary" onclick={onSearch}>Search</InputGroup.Button>
	</InputGroup.Addon>
</InputGroup.Root>
