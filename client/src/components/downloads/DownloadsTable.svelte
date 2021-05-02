
<script lang="ts">
    import DownloadsTableItem from "./DownloadsTableItem.svelte"
    import type { DownloadInfo } from "../../utils/types"

    export let downloadsInfo: { [key: string]: DownloadInfo }
</script>
    
<div class="flex flex-col mt-4">
    <div class="overflow-x-auto sm:-mx-6 lg:-mx-8">
        <div class="py-2 align-middle inline-block min-w-full sm:px-6 lg:px-8">
            <div class="shadow overflow-hidden border-b border-gray-200 sm:rounded-lg">
                <table class="min-w-full divide-y divide-gray-200">
                    <thead class="bg-gray-50">
                        <tr>
                            <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                            </th>
                            <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                                Info
                            </th>
                            <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                                Status
                            </th>
                            <th scope="col" class="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">
                            </th>
                        </tr>
                    </thead>
                    <tbody class="bg-white divide-y divide-gray-200">
                        {#if Object.keys(downloadsInfo)?.length > 0}
                        {#each Object.values(downloadsInfo) as downloadInfo (downloadInfo.url)}
                            <DownloadsTableItem {downloadInfo} />
                        {/each}
                        {:else}
                        <tr class="content-center px-6 py-4 inline-block align-middle text-gray-500">
                            No Downloads
                        </tr>
                        {/if}
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</div>