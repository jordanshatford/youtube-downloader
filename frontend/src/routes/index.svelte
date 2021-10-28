<script lang="ts">
	import Title from '$lib/components/typography/Title.svelte'
	import Description from '$lib/components/typography/Description.svelte'
	import { search } from '$lib/stores/search'
	import SearchBar from '$lib/components/ui/SearchBar.svelte'
	import ResultCard from '$lib/components/search/ResultCard.svelte'

	function searchVideos(event: CustomEvent) {
		let term = event.detail.term
		search.get(term)
	}
</script>

<svelte:head>
	<title>Search - Youtube to MP3</title>
</svelte:head>

<div>
	<Title>Search</Title>
	<Description>Search Youtube for the videos you want to download to MP3</Description>
	<div class="max-w-xl mx-auto rounded-lg overflow-hidden md:max-w-xl">
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
