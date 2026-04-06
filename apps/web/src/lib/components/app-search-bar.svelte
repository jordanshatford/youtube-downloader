<script lang="ts">
	import { InputGroup, SearchIcon, SpinnerIcon } from '@yd/ui';

	interface Props {
		results?: number;
		loading?: boolean;
		query: string;
		onsearch: (query: string) => void | Promise<void>;
	}

	let { results, loading = false, query = $bindable(), onsearch }: Props = $props();

	function search(event: KeyboardEvent) {
		if (event.key === 'Enter' && query.length > 0) {
			onsearch(query);
		}
	}
</script>

<InputGroup.Root>
	<InputGroup.Input
		placeholder="Search..."
		bind:value={query}
		disabled={loading}
		onkeypress={search}
		type="search"
	/>
	<InputGroup.Addon>
		{#if loading}
			<SpinnerIcon />
		{:else}
			<SearchIcon />
		{/if}
	</InputGroup.Addon>
	{#if results && results > 0}
		<InputGroup.Addon align="inline-end">{results} result(s)</InputGroup.Addon>
	{/if}
</InputGroup.Root>
