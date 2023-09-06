<script lang="ts">
	import { Title, Description } from '@yd/ui';
	import { search } from '$lib/stores/search';
	import SearchBar from '$lib/components/SearchBar.svelte';
	import ResultCard from '$lib/components/ResultCard.svelte';
	import config from '$lib/config';

	async function searchVideos(event: CustomEvent<{ term: string }>) {
		await search.get(event.detail.term);
	}
</script>

<svelte:head>
	<title>Search - {config.about.title}</title>
</svelte:head>

<div>
	<Title>Search</Title>
	<Description>Search YouTube for the videos you want to download and convert to audio</Description>
	<div class="max-w-xl mx-auto overflow-hidden md:max-w-xl">
		<div class="md:flex">
			<div class="w-full mt-4">
				<SearchBar on:search={searchVideos} loading={$search.loading} searchTerm={$search.term} />
			</div>
		</div>
	</div>
	<div class="container mt-8 pb-8 mx-auto px-4 md:px-12">
		<div class="flex flex-wrap -mx-1 lg:-mx-4">
			{#each $search.results as result (result.id)}
				<ResultCard {result} />
			{/each}
		</div>
	</div>
</div>
