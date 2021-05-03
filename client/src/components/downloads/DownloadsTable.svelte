
<script lang="ts">
    import { trash, download } from "svelte-awesome/icons"
    import IconButton from "../lib/IconButton.svelte"
    import StatusBadge from "../lib/StatusBadge.svelte"
    import { downloadsStore } from "../../stores/downloads"
    import { truncate } from "../../utils/functions"
    import { MAX_TITLE_LENGTH } from "../../utils/constants"
    import { Status } from "../../utils/types"
    import type { DownloadInfo } from "../../utils/types"

    export let downloads: { [key: string]: DownloadInfo }
</script>

<table class="min-w-full divide-y divide-gray-800 table-auto">
    <thead class="bg-gray-800">
        <tr>
            <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-white uppercase">
                Info
            </th>
            <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-white uppercase">
                Status
            </th>
            <th scope="col" class="px-6 py-3 text-right text-xs font-medium text-white uppercase">
                Actions
            </th>
        </tr>
    </thead>
    <tbody class="bg-gray-700 divide-y divide-gray-800">
        {#each Object.values(downloads) as downloadInfo (downloadInfo.id)}
        <tr>
            <td class="px-6 py-4 whitespace-nowrap">
                <div class="flex items-center">
                    <div class="hidden md:block flex-shrink-0 h-10 w-18">
                        <img class="h-10 w-18" src="{downloadInfo.thumbnail}" alt="Thumbnail">
                    </div>
                    <div class="md:ml-4">
                        <div class="text-sm font-medium text-white">
                            {truncate(downloadInfo.title, MAX_TITLE_LENGTH)}
                        </div>
                        <div class="text-sm text-gray-400 underline">
                            <a href="{downloadInfo.url}" target="_blank">Link</a>
                        </div>
                    </div>
                </div>
            </td>
            <td class="px-6 py-4 whitespace-nowrap">
                <StatusBadge status={downloadInfo.status} />
            </td>
            <td class="px-6 py-4 whitespace-nowrap text-gray-500 text-right">
                <IconButton
                    className="hover:text-red-500 hover:scale-110"
                    iconScale={1.25}
                    disabled={downloadInfo.status !== Status.DONE}
                    data={trash}
                    on:click={_ => downloadsStore.removeDownload(downloadInfo.id)}
                />
                <IconButton
                    className="hover:text-purple-500 hover:scale-110"
                    iconScale={1.25}
                    disabled={downloadInfo.status !== Status.DONE}
                    data={download}
                    on:click={_ => downloadsStore.downloadAudioFile(downloadInfo.id)}
                />
            </td>
        </tr>
        {/each}
    </tbody>
</table>
