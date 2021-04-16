<script>
    import Icon from "svelte-awesome"
    import { times } from "svelte-awesome/icons"
    import StatusBadge from "./StatusBadge.svelte"
    import { downloadsStore } from "../../stores/downloads.js"

    const MAX_TITLE_LENGTH = 30

    export let downloadInfo
    
    function removeVideo() {
        downloadsStore.removeDownload(downloadInfo.url)
    }

    function downloadVideoAudio() {
        console.error("Downloading videos is not implemented yet!")
    }
</script>

<tr>
    <td class="px-6 py-4 whitespace-nowrap text-gray-500">
        <button on:click={removeVideo} class="border-none outline-none focus:outline-none mr-1 mb-2 ease-linear transition-all duration-150" type="button">
            <Icon data={times} class="text-red-500" /> 
        </button>
    </td>
    <td class="px-6 py-4 whitespace-nowrap">
        <div class="flex items-center">
            <div class="flex-shrink-0 h-10 w-18">
                <img class="h-10 w-18" src="{downloadInfo.thumbnail}" alt="Thumbnail">
            </div>
            <div class="ml-4">
            <div class="text-sm font-medium text-gray-900">
                {downloadInfo.title.substring(0, MAX_TITLE_LENGTH) + "..."}
            </div>
            <div class="text-sm text-gray-500 underline">
                <a href="{downloadInfo.url}" target="_blank">Link</a>
            </div>
            </div>
        </div>
    </td>
    <td class="px-6 py-4 whitespace-nowrap">
        <StatusBadge statusValue={downloadInfo.downloading} />
    </td>
    <td class="px-6 py-4 whitespace-nowrap">
        <StatusBadge statusValue={downloadInfo.processing} />
    </td>
    <td class="px-6 py-4 whitespace-nowrap text-right text-sm">
        <!-- <a href="{downloadInfo.downloadLink}" disabled download class="text-indigo-600 hover:text-indigo-900 hover:no-underline">Download</a> -->
        {#if downloadInfo.readyForDownload}
        <button on:click={downloadVideoAudio} class="border-none outline-none text-sm font-medium focus:outline-none hover:no-underline text-indigo-600 hover:text-indigo-900" type="button">
            Download
        </button>
        {:else}
        <p class="text-grey-100">Not Ready</p>
        {/if}
    </td>
</tr>