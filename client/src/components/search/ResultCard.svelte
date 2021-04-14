<script>
    import IconButton from '../base/IconButton.svelte'
    import { download } from 'svelte-awesome/icons'

    const DESCRIPTION_MAX_LENGTH = 75

    export let result

    $: minutes = Math.floor(result.duration / 60)
    $: seconds = result.duration - (minutes * 60)

    function downloadVideo() {
        console.error("Downloading video audio not implemented yet!")
    }
</script>


<div class="my-1 px-1 w-full md:w-1/2 lg:my-4 lg:px-4 lg:w-1/3">
    <article class="overflow-hidden rounded-lg shadow-lg">
        <a href="{result.webpage_url}" target="_blank">
            <img alt="Thumbnail" class="block h-auto w-full" src="{result.thumbnail}">
        </a>
        <header class="flex items-center justify-between leading-tight p-2 md:p-4">
            <h1 class="text-lg">
                <a class="no-underline hover:underline text-black" href="{result.webpage_url}" target="_blank">
                    {result.title}
                </a>
            </h1>
            <p class="text-grey-darker text-sm">{`${minutes}:${seconds}`}</p>
        </header>
        <div class="flex items-center justify-between leading-tight p-2 md:p-4">
            <p class="text-grey-darker text-sm">{result.description.substring(0, DESCRIPTION_MAX_LENGTH) + "..."}</p>
        </div>
        <footer class="flex items-center justify-between leading-none p-2 md:p-4">
            <a class="flex items-center no-underline hover:underline text-black" href="{result.channel_url}" target="_blank">
                <p class="ml-2 text-sm">
                    {result.channel}
                </p>
            </a>
            <IconButton on:click={downloadVideo} data={download} />
        </footer>
    </article>
</div>
