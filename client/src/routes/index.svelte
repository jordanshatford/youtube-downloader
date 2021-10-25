<script lang="ts">
	import Heading from '$lib/components/typography/Heading.svelte'
	import Title from '$lib/components/typography/Title.svelte'
	import Description from '$lib/components/typography/Description.svelte'
	import { search } from '$lib/stores/search'
	import SearchBar from '$lib/components/search/SearchBar.svelte'
	import ResultCard from '$lib/components/search/ResultCard.svelte'
	import NoResults from '$lib/components/search/NoResults.svelte'

	function searchVideos(event: CustomEvent) {
		let term = event.detail.term
		search.get(term)
	}
</script>

<svelte:head>
	<title>Search - Youtube to MP3</title>
</svelte:head>

<div>
	<Heading>Youtube to MP3</Heading>
	<Title>Search Videos</Title>
	<Description>Search for the videos you want to convert to MP3.</Description>
	<div class="max-w-xl mx-auto rounded-lg overflow-hidden md:max-w-xl">
		<div class="md:flex">
			<div class="w-full">
				<SearchBar on:search={searchVideos} loading={$search.loading} searchTerm={$search.term} />
			</div>
		</div>
	</div>
	<div class="container mt-8 pb-8 mx-auto px-4 md:px-12">
		<div class="flex flex-wrap -mx-1 lg:-mx-4">
			{#each $search.results as result (result.id)}
				<ResultCard {result} />
			{:else}
				{#if $search.term != '' && !$search.loading}
					<NoResults />
				{/if}
			{/each}
		</div>
	</div>
</div>
