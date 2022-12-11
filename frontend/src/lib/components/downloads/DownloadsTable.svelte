<script lang="ts">
	import StatusBadge from '$lib/components/StatusBadge.svelte'
	import DownloadActions from '$lib/components/downloads/DownloadActions.svelte'
	import { downloads } from '$lib/stores/downloads'
	import type { VideoInfo } from '$lib/utils/types'

	export let items: Record<string, VideoInfo>
</script>

<table class="min-w-full divide-y divide-zinc-200 dark:divide-zinc-800 table-auto">
	<thead class="bg-zinc-50 dark:bg-zinc-800">
		<tr>
			<th
				scope="col"
				class="px-6 py-3 text-left text-xs font-medium text-zinc-500 dark:text-white uppercase"
			>
				Info
			</th>
			<th
				scope="col"
				class="px-6 py-3 text-left text-xs font-medium text-zinc-500 dark:text-white uppercase"
			>
				Status
			</th>
			<th
				scope="col"
				class="px-6 py-3 text-right text-xs font-medium text-zinc-500 dark:text-white uppercase"
			>
				Actions
			</th>
		</tr>
	</thead>
	<tbody class="bg-white dark:bg-zinc-900 divide-y divide-zinc-200 dark:divide-zinc-800">
		{#each Object.values(items) as downloadInfo (downloadInfo.id)}
			<tr>
				<td class="px-6 py-4 whitespace-nowrap">
					<div class="flex items-center">
						<div class="hidden md:block flex-shrink-0 h-10 w-18">
							<img class="h-10 w-18 rounded-lg" src={downloadInfo.thumbnail} alt="Thumbnail" />
						</div>
						<div class="md:ml-4 lg:max-w-lg md:max-w-xs sm:max-w-xxs max-w-xxxs truncate">
							<div class="text-sm truncate font-medium text-zinc-800 dark:text-white">
								{downloadInfo.title}
							</div>
							<div class="text-sm text-zinc-500 dark:text-zinc-400 underline">
								<a href={downloadInfo.url} target="_blank" rel="noreferrer">Link</a>
							</div>
						</div>
					</div>
				</td>
				<td class="px-6 py-4 whitespace-nowrap">
					<StatusBadge status={downloadInfo.status} />
				</td>
				<td class="px-6 py-4 whitespace-nowrap text-zinc-500 dark:text-zinc-300 text-right">
					<DownloadActions
						status={downloadInfo.status}
						awaitingFileBlob={downloadInfo.awaitingFileBlob}
						on:delete={() => downloads.remove(downloadInfo.id)}
						on:restart={() => {
							downloads.remove(downloadInfo.id)
							downloads.add(downloadInfo)
						}}
						on:download={() => downloads.getFile(downloadInfo.id)}
					/>
				</td>
			</tr>
		{/each}
	</tbody>
</table>
