<script lang="ts">
	import DownloadActions from '$lib/components/DownloadActions.svelte';
	import NotFound from '$lib/components/NotFound.svelte';
	import StatusBadge from '$lib/components/StatusBadge.svelte';
	import config from '$lib/config';
	import { downloads } from '$lib/stores/downloads';
	import { userSettings } from '$lib/stores/settings';

	import { Badge, Pagination, Table, Title } from '@yd/ui';

	let page = $state(1);

	let pageSize = $derived($userSettings.downloadsPageSize);
	let totalDownloads = $derived(Object.keys($downloads).length);
	let totalPages = $derived(Math.ceil(totalDownloads / pageSize));
	let start = $derived((page - 1) * pageSize);
	let currentPageDownloads = $derived(Object.values($downloads).slice(start, start + pageSize));

	const columns = [
		{
			key: 'info',
			title: 'Info'
		},
		{
			key: 'format',
			title: 'Format'
		},
		{
			key: 'state',
			title: 'State'
		},
		{
			key: 'actions',
			title: 'Actions'
		}
	];
</script>

<svelte:head>
	<title>Downloads - {config.head.title}</title>
</svelte:head>

{#if totalDownloads === 0}
	<NotFound
		title="Error"
		subtitle="No downloads found."
		description="Try adding new downloads via the search page."
	/>
{:else}
	<div>
		<Title>Downloads</Title>
		<div class="mt-4 flex flex-col">
			<div class="overflow-x-auto sm:-mx-6 lg:-mx-8">
				<div class="inline-block min-w-full py-2 align-middle sm:px-6 lg:px-8">
					<div
						class="overflow-hidden rounded-lg border border-zinc-200 shadow dark:border-zinc-800 dark:shadow-dark"
					>
						<Table {columns} rows={currentPageDownloads}>
							{#snippet cell({ column, row })}
								<span>
									{#if column.key === 'info'}
										<a href={row.video.url} target="_blank" class="flex items-center">
											<div class="w-18 hidden h-10 flex-shrink-0 md:block">
												<img
													class="w-18 h-10 rounded-lg"
													src={row.video.thumbnail}
													alt="Thumbnail"
												/>
											</div>
											<div class="sm:max-w-xxs max-w-xxxs truncate md:ml-4 md:max-w-xs lg:max-w-lg">
												<div class="truncate text-sm font-medium text-zinc-800 dark:text-white">
													{row.video.title}
												</div>
												<div class="text-sm text-zinc-500 dark:text-zinc-400">
													{row.video.channel.name}
												</div>
											</div>
										</a>
									{:else if column.key === 'format'}
										<Badge>{row.options.format.toUpperCase()}</Badge>
									{:else if column.key === 'state'}
										<StatusBadge status={row.status} />
									{:else if column.key === 'actions'}
										<DownloadActions download={row} />
									{/if}
								</span>
							{/snippet}
						</Table>
					</div>
					<Pagination bind:page {totalPages} class="py-4" />
				</div>
			</div>
		</div>
	</div>
{/if}
