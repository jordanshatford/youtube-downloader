
<script lang="ts">
    import DownloadsTableItem from "./DownloadsTableItem.svelte"
    import type { DownloadInfo } from "../../utils/types"

    export let downloadsInfo: { [key: string]: DownloadInfo }
</script>
    
<div class="flex flex-col mt-4">
    <div class="overflow-x-auto sm:-mx-6 lg:-mx-8">
        <div class="py-2 align-middle inline-block min-w-full sm:px-6 lg:px-8">
            <div class="shadow overflow-hidden border-b border-gray-800 sm:rounded-lg">
                <table class="min-w-full divide-y divide-gray-800">
                    <thead class="bg-gray-800">
                        <tr>
                            <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-white uppercase tracking-wider">
                            </th>
                            <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-white uppercase tracking-wider">
                                Info
                            </th>
                            <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-white uppercase tracking-wider">
                                Status
                            </th>
                            <th scope="col" class="px-6 py-3 text-right text-xs font-medium text-white uppercase tracking-wider">
                            </th>
                        </tr>
                    </thead>
                    <tbody class="bg-gray-700 divide-y divide-gray-800">
                        {#if Object.keys(downloadsInfo)?.length > 0}
                        {#each Object.values(downloadsInfo) as downloadInfo (downloadInfo.url)}
                            <DownloadsTableItem {downloadInfo} />
                        {/each}
                        {:else}
                        <tr class="content-center px-6 py-4 inline-block align-middle text-white">
                            No Downloads
                        </tr>
                        {/if}
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</div>