<svelte:head>
	<title>Search - Youtube to MP3</title>
</svelte:head>

<script lang="ts">
    import Heading from "../lib/typography/Heading.svelte"
    import Title from "../lib/typography/Title.svelte"
    import Description from "../lib/typography/Description.svelte"
    import { search } from "../stores/search"
    import SearchBar from "../lib/search/SearchBar.svelte"
    import ResultCard from "../lib/search/ResultCard.svelte"
    import NoResults from "../lib/search/NoResults.svelte"

    function searchVideos(event: CustomEvent) {
        let term = event.detail.searchTerm
        search.get(term)
	}
</script>

<div>
    <Heading>Youtube to MP3</Heading>
    <Title>Search Videos</Title>
    <Description>Search for the videos you want to convert to MP3.</Description>
    <SearchBar
        on:search={searchVideos}
        loading={$search.loading}
        searchTerm={$search.term}
    />
    <div class="container mt-8 pb-8 mx-auto px-4 md:px-12">
        <div class="flex flex-wrap -mx-1 lg:-mx-4">
            {#each $search.results as result (result.id)}
                <ResultCard result={result} />
            {:else}
                {#if ($search.term != "" && !$search.loading)}
                    <NoResults />
                {/if}
            {/each}
        </div>
    </div>
</div>
