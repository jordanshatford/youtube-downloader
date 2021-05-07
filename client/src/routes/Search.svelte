<svelte:head>
	<title>Search Videos - Youtube to MP3</title>
</svelte:head>

<script lang="ts">
    import Heading from "../components/typography/Heading.svelte"
    import Title from "../components/typography/Title.svelte"
    import Description from "../components/typography/Description.svelte"
    import { searchStore } from "../stores/search.js"
    import SearchBar from "../components/search/SearchBar.svelte"
    import VideoResults from "../components/search/VideoResults.svelte"

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
