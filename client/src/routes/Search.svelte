<svelte:head>
	<title>Search Videos - Youtube to MP3</title>
</svelte:head>

<script lang="ts">
    import Heading from "../lib/typography/Heading.svelte"
    import Title from "../lib/typography/Title.svelte"
    import Description from "../lib/typography/Description.svelte"
    import { searchStore } from "../stores/search.js"
    import SearchBar from "../lib/search/SearchBar.svelte"
    import VideoResults from "../lib/search/VideoResults.svelte"

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
    <VideoResults results={$searchStore.results} />
</div>
