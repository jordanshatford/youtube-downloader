<svelte:head>
	<title>Downloads - Youtube to MP3</title>
</svelte:head>

<script>
    import DownloadsTable from "../components/downloads/DownloadsTable.svelte"

    let videos = {
        "https://www.youtube.com/watch?v=uK2RnIzrQ0M" : {
            downloadLink: "Svelte_Crash_Course.mp3",
            title: "Svelte Crash Course",
            thumbnail: "https://i.ytimg.com/vi_webp/uK2RnIzrQ0M/maxresdefault.webp",
            url: "https://www.youtube.com/watch?v=uK2RnIzrQ0M",
            downloading: "IN PROGRESS",
            processing: "WAITING",
            readyForDownload: false,
        },
    }
</script>

<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <h2 class="text-center text-base text-indigo-600 font-semibold tracking-wide uppercase">Youtube To MP3</h2>
    <p class="text-center mt-4 max-w-2xl text-xl text-gray-500 mx-auto">
        Here are all the videos you have downloaded to MP3.
    </p>
    <DownloadsTable downloadsInfo={videos} />
</div>
