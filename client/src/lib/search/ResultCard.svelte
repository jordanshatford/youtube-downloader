<script lang="ts">
    import IconButton from "../IconButton.svelte"
    import { download } from "../icons"
    import { downloads } from "../../stores/downloads"
    import { truncate } from "../../utils/functions"
    import { DESCRIPTION_MAX_LENGTH } from "../../utils/constants"
    import type { VideoInfo } from "../../utils/types"
    import { Status } from "../../utils/types"

    export let result: VideoInfo
</script>


<div class="my-1 px-1 w-full md:w-1/2 lg:my-4 lg:px-4 lg:w-1/3">
    <article class="dark:bg-gray-800 overflow-hidden rounded-lg shadow-lg">
        <a href="{result.url}" target="_blank">
            <img alt="Thumbnail" class="block h-auto w-full" src="{result.thumbnail}">
        </a>
        <header class="flex items-center justify-between leading-tight p-2 md:p-4">
            <h1 class="text-lg">
                <a class="no-underline hover:underline text-gray-900 dark:text-white" href="{result.url}" target="_blank">
                    {result.title}
                </a>
            </h1>
            <p class="text-gray-700 dark:text-gray-300 text-sm">{result.duration}</p>
        </header>
        <div class="flex items-center justify-between leading-tight p-2 md:p-4">
            <p class="text-gray-800 dark:text-gray-400 text-sm">{truncate(result.description, DESCRIPTION_MAX_LENGTH)}</p>
        </div>
        <footer class="flex items-center justify-between leading-none p-2 md:p-4">
            <p class="flex items-center text-sm text-black dark:text-white">
                {result.channel}
            </p>
            {#if !(result.id in $downloads)}
                <IconButton
                    on:click={_ => downloads.add({ ...result, "status": Status.WAITING })}
                    data={download}
                    className="text-black dark:text-white hover:text-purple-500 dark:hover:text-purple-500"
                    size={1.25}
                />
            {/if}
        </footer>
    </article>
</div>
