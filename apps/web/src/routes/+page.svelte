<script lang="ts">
	import AppResultItem from '$lib/components/app-result-item.svelte';
	import AppSearchBar from '$lib/components/app-search-bar.svelte';
	import config from '$lib/config';
	import { search } from '$lib/stores/search.svelte';

	import { Button, Empty, Item, SearchIcon, SpinnerIcon } from '@yd/ui';
</script>

<svelte:head>
	<title>Search - {config.head.title}</title>
</svelte:head>

<AppSearchBar
	query={search.query}
	loading={search.loading}
	onsearch={(query) => search.get(query)}
	results={search.results.length}
/>
{#if search.results.length > 0}
	<div class="mt-4">
		<Item.Group>
			{#each search.results as result, i (i)}
				<AppResultItem {result} />
			{/each}
		</Item.Group>
		<div class="flex w-full justify-center pt-4">
			<Button.Root
				variant="outline"
				class="inline-flex items-center gap-2"
				onclick={() => search.getMore()}
				disabled={search.loading}
			>
				{#if search.loading}
					<SpinnerIcon class="size-5" />
				{/if}
				<span>{search.loading ? 'Searching' : 'Get more'}</span></Button.Root
			>
		</div>
	</div>
{:else}
	<Empty.Root>
		<Empty.Header>
			<Empty.Media variant="icon">
				<SearchIcon />
			</Empty.Media>
			<Empty.Title>No results yet.</Empty.Title>
			<Empty.Description>
				Search using the above search bar to find videos to download. You can search by video title,
				channel name, or URL.
			</Empty.Description>
		</Empty.Header>
	</Empty.Root>
{/if}
