<svelte:head>
	<title>Search - Youtube to MP3</title>
</svelte:head>

<script lang="ts">
    import Heading from "../lib/typography/Heading.svelte"
    import Title from "../lib/typography/Title.svelte"
    import Description from "../lib/typography/Description.svelte"
    import { searchStore } from "../stores/search"
    import SearchBar from "../lib/search/SearchBar.svelte"
    import ResultCard from "../lib/search/ResultCard.svelte"
    import NoResults from "../lib/search/NoResults.svelte"

    function fetchVideos(event: CustomEvent) {
        let term = event.detail.searchTerm
        let numberResults = event.detail.numberResults
        searchStore.search(term, numberResults)
	}
</script>

<div>
    <Heading>Youtube to MP3</Heading>
    <Title>Search Videos</Title>
    <Description>Search for the videos you want to convert to MP3.</Description>
    <SearchBar
        on:search={fetchVideos}
        disabled={$searchStore.loading}
        searchTerm={$searchStore.term}
        numberResults={$searchStore.numberResults}
    />
    <div class="container mt-8 pb-8 mx-auto px-4 md:px-12">
        <div class="flex flex-wrap -mx-1 lg:-mx-4">
            {#each $searchStore.results as result (result.id)}
                <ResultCard result={result} />
            {:else}
                {#if ($searchStore.term != "" && !$searchStore.loading)}
                    <NoResults />
                {/if}
            {/each}
        </div>
    </div>
</div>
