<script lang="ts">
	import { Title } from '@yd/ui';
	import { search } from '$lib/stores/search';
	import SearchBar from '$lib/components/SearchBar.svelte';
	import ResultCard from '$lib/components/ResultCard.svelte';
	import config from '$lib/config';

	async function searchVideos(event: CustomEvent<{ term: string }>) {
		await search.get(event.detail.term);
	}
</script>

<svelte:head>
	<title>Search - {config.head.title}</title>
</svelte:head>

<div>
	<Title>Search</Title>
	<div class="mx-auto max-w-xl overflow-hidden md:max-w-xl">
		<div class="md:flex">
			<div class="mt-4 w-full">
				<SearchBar on:search={searchVideos} loading={$search.loading} searchTerm={$search.term} />
			</div>
		</div>
	</div>
	<div class="container mx-auto mt-8 px-4 pb-8 md:px-12">
		<div class="-mx-1 flex flex-wrap lg:-mx-4">
			{#each $search.results as result (result.id)}
				<ResultCard {result} />
			{/each}
		</div>
	</div>
</div>
