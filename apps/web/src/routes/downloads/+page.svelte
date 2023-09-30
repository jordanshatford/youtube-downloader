<script lang="ts">
	import { Badge, Pagination, Table, Title } from '@yd/ui';
	import { downloads } from '$lib/stores/downloads';
	import DownloadActions from '$lib/components/DownloadActions.svelte';
	import NoDownloads from '$lib/components/NoDownloads.svelte';
	import StatusBadge from '$lib/components/StatusBadge.svelte';
	import config from '$lib/config';

	let page = 1;
	let pageSize = 10;

	$: totalDownloads = Object.keys($downloads).length;
	$: totalPages = Math.ceil(totalDownloads / pageSize);
	$: start = (page - 1) * pageSize;
	$: currentPageDownloads = Object.values($downloads).slice(start, start + pageSize);

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
	<NoDownloads />
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
							<span slot="cell" let:column let:row>
								{#if column.key === 'info'}
									<div class="flex items-center">
										<div class="w-18 hidden h-10 flex-shrink-0 md:block">
											<img class="w-18 h-10 rounded-lg" src={row.thumbnail} alt="Thumbnail" />
										</div>
										<div class="sm:max-w-xxs max-w-xxxs truncate md:ml-4 md:max-w-xs lg:max-w-lg">
											<div class="truncate text-sm font-medium text-zinc-800 dark:text-white">
												{row.title}
											</div>
											<div class="text-sm text-zinc-500 underline dark:text-zinc-400">
												<a href={row.url} target="_blank" rel="noreferrer">Link</a>
											</div>
										</div>
									</div>
								{:else if column.key === 'format'}
									<Badge>{row.options.format.toUpperCase()}</Badge>
								{:else if column.key === 'state'}
									<StatusBadge status={row.status} />
								{:else if column.key === 'actions'}
									<DownloadActions video={row} />
								{/if}
							</span>
						</Table>
					</div>
					<Pagination bind:page {totalPages} class="py-4" />
				</div>
			</div>
		</div>
	</div>
{/if}
