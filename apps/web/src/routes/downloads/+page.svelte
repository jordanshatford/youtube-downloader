<script lang="ts">
	import { DownloadState } from '@yd/client';
	import { DownloadIcon, LoaderIcon, RotateIcon, TrashIcon, Pagination } from '@yd/ui';
	import { Confirm, Badge, IconButton, Table, Title, Description } from '@yd/ui';
	import { downloads } from '$lib/stores/downloads';
	import StatusBadge from '$lib/components/StatusBadge.svelte';
	import config from '$lib/config';

	let page = 1;
	let pageSize = 10;

	$: totalPages = Math.ceil(Object.keys($downloads).length / pageSize);
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
	<title>Downloads - {config.about.title}</title>
</svelte:head>

<div>
	<Title>Downloads</Title>
	<Description>View videos being downloaded and converted.</Description>
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
								<div>
									{#if [DownloadState.DONE, DownloadState.ERROR].includes(row.status.state)}
										<Confirm
											variant="error"
											title="Delete download?"
											description="Are you sure you want to delete this download? Deleting is permanent."
											cancelText="Cancel"
											confirmText="Delete"
											let:confirm={onConfirm}
										>
											<IconButton
												on:click={() => onConfirm(() => downloads.remove(row.id))}
												src={TrashIcon}
												class="mr-2 h-10 w-10 hover:text-red-600"
											/>
										</Confirm>
									{/if}
									{#if [DownloadState.ERROR].includes(row.status.state)}
										<IconButton
											on:click={async () => await downloads.restart(row.id)}
											src={RotateIcon}
											class="h-10 w-10 hover:text-indigo-800 dark:hover:text-indigo-600"
										/>
									{:else if row.status.state === DownloadState.DONE}
										{#if row.awaitingFileBlob}
											<IconButton src={LoaderIcon} class="h-10 w-10 animate-spin" />
										{:else}
											<IconButton
												on:click={async () => await downloads.getFile(row.id)}
												src={DownloadIcon}
												class="h-10 w-10 hover:text-indigo-800 dark:hover:text-indigo-600"
											/>
										{/if}
									{/if}
								</div>
							{/if}
						</span>
					</Table>
				</div>
				<Pagination bind:page {totalPages} class="py-4" />
			</div>
		</div>
	</div>
</div>
