<svelte:head>
	<title>Downloads - Youtube to MP3</title>
</svelte:head>

<script>
    import { downloadsStore } from "../stores/downloads.js"
    import DownloadsTable from "../components/downloads/DownloadsTable.svelte"
</script>

<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <h2 class="text-center text-base text-indigo-600 font-semibold tracking-wide uppercase">Youtube To MP3</h2>
    <p class="text-center mt-4 max-w-2xl text-xl text-gray-500 mx-auto">
        Here are all the videos you have downloaded to MP3.
    </p>
    <DownloadsTable downloadsInfo={$downloadsStore} />
</div>
