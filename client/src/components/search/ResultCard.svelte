<script lang="ts">
    import IconButton from "../lib/IconButton.svelte"
    import { download } from "svelte-awesome/icons"

    import { downloadsStore } from "../../stores/downloads"
    import { formatSeconds, truncate } from "../../utils/functions"
    import { DESCRIPTION_MAX_LENGTH } from "../../utils/constants"
    import { YoutubeDownloadInfo } from "../../utils/classes"
    import type { SearchResult } from "../../utils/types"

    export let result: SearchResult

    $: duration = formatSeconds(result.duration)
</script>


<div class="my-1 px-1 w-full md:w-1/2 lg:my-4 lg:px-4 lg:w-1/3">
    <article class="bg-gray-800 overflow-hidden rounded-lg shadow-lg">
        <a href="{result.webpage_url}" target="_blank">
            <img alt="Thumbnail" class="block h-auto w-full" src="{result.thumbnail}">
        </a>
        <header class="flex items-center justify-between leading-tight p-2 md:p-4">
            <h1 class="text-lg">
                <a class="no-underline hover:underline text-white" href="{result.webpage_url}" target="_blank">
                    {result.title}
                </a>
            </h1>
            <p class="text-gray-300 text-sm">{duration}</p>
        </header>
        <div class="flex items-center justify-between leading-tight p-2 md:p-4">
            <p class="text-gray-400 text-sm">{truncate(result.description, DESCRIPTION_MAX_LENGTH)}</p>
        </div>
        <footer class="flex items-center justify-between leading-none p-2 md:p-4">
            <a class="flex items-center no-underline hover:underline text-white" href="{result.channel_url}" target="_blank">
                <p class="ml-2 text-sm">
                    {result.channel}
                </p>
            </a>
            <IconButton
                on:click={_ => downloadsStore.addDownload(YoutubeDownloadInfo.fromSearchResult(result))}
                data={download}
                className="hover:text-purple-500 hover:scale-110"
                iconScale={1.25}
                disabled={result.id in $downloadsStore}
            />
        </footer>
    </article>
</div>
