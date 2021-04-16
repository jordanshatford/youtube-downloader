<svelte:head>
	<title>Search Videos - Youtube to MP3</title>
</svelte:head>

<script>
    import { searchStore } from "../stores/search.js"
    import SearchBar from "../components/search/SearchBar.svelte"
    import VideoResults from "../components/search/VideoResults.svelte"

    function fetchVideos(event) {
        let term = event.detail.searchTerm
        let numberResults = event.detail.numberResults
        searchStore.search(term, numberResults)
	}
</script>

<div>
    <h2 class="text-center text-base text-indigo-600 font-semibold tracking-wide uppercase">Youtube To MP3</h2>
    <p class="text-center mt-2 text-3xl leading-8 font-extrabold tracking-tight text-gray-900 sm:text-4xl">
        Convert Youtube videos to MP3
    </p>
    <p class="text-center mt-4 max-w-2xl text-xl text-gray-500 mx-auto">
        Search for the videos you want and convert multiple to MP3 at a time.
    </p>
    <div class="max-w-xl mx-auto rounded-lg overflow-hidden md:max-w-xl">
        <div class="md:flex">
            <div class="w-full p-3">
                <div class="relative">
                    <SearchBar on:search={fetchVideos} disabled={$searchStore.loading} />
                </div>
            </div>
        </div>
    </div>
    <VideoResults results={$searchStore.results} />
</div>
