<script lang="ts">
	import { Trash2Icon, DownloadIcon, LoaderIcon, RotateCwIcon } from 'svelte-feather-icons';
	import { Status } from '@yad/client';
	import IconButton from '$lib/components/ui/IconButton.svelte';
	import Title from '$lib/components/typography/Title.svelte';
	import Tag from '$lib/components/ui/Tag.svelte';
	import Description from '$lib/components/typography/Description.svelte';
	import { downloads } from '$lib/stores/downloads';
	import StatusBadge from '$lib/components/StatusBadge.svelte';
	import config from '$lib/config';
	import Table from '$lib/components/Table.svelte';
	import Confirm from '$lib/components/ui/Confirm.svelte';

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
			key: 'status',
			title: 'Status'
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
	<Description>View videos being converted</Description>
	<div class="flex flex-col mt-4">
		<div class="overflow-x-auto sm:-mx-6 lg:-mx-8">
			<div class="py-2 align-middle inline-block min-w-full sm:px-6 lg:px-8">
				<div
					class="rounded-lg shadow dark:shadow-dark overflow-hidden border border-zinc-200 dark:border-zinc-800"
				>
					<Table {columns} rows={Object.values($downloads)}>
						<span slot="cell" let:column let:row>
							{#if column.key === 'info'}
								<div class="flex items-center">
									<div class="hidden md:block flex-shrink-0 h-10 w-18">
										<img class="h-10 w-18 rounded-lg" src={row.thumbnail} alt="Thumbnail" />
									</div>
									<div class="md:ml-4 lg:max-w-lg md:max-w-xs sm:max-w-xxs max-w-xxxs truncate">
										<div class="text-sm truncate font-medium text-zinc-800 dark:text-white">
											{row.title}
										</div>
										<div class="text-sm text-zinc-500 dark:text-zinc-400 underline">
											<a href={row.url} target="_blank" rel="noreferrer">Link</a>
										</div>
									</div>
								</div>
							{:else if column.key === 'format'}
								<Tag>{row.options.format.toUpperCase()}</Tag>
							{:else if column.key === 'status'}
								<StatusBadge status={row.status} />
							{:else if column.key === 'actions'}
								<div>
									{#if [Status.DONE, Status.ERROR, Status.UNDEFINED].includes(row.status)}
										<Confirm
											title="Delete Audio?"
											description="Are you sure you want to delete this audio? Deleting is permanent."
											cancelText="Cancel"
											confirmText="Delete"
											let:confirm={onConfirm}
										>
											<IconButton
												on:click={() => onConfirm(downloads.remove, row.id)}
												icon={Trash2Icon}
												size="1.5x"
												class="hover:text-red-600 mr-2"
											/>
										</Confirm>
									{/if}
									{#if [Status.ERROR, Status.UNDEFINED].includes(row.status)}
										<IconButton
											on:click={() => {
												downloads.remove(row.id);
												downloads.add(row);
											}}
											icon={RotateCwIcon}
											size="1.5x"
											class="hover:text-indigo-800 dark:hover:text-indigo-600"
										/>
									{:else if row.status === Status.DONE}
										{#if row.awaitingFileBlob}
											<IconButton icon={LoaderIcon} size="1.5x" class="animate-spin" />
										{:else}
											<IconButton
												on:click={async () => await downloads.getFile(row.id)}
												icon={DownloadIcon}
												size="1.5x"
												class="hover:text-indigo-800 dark:hover:text-indigo-600"
											/>
										{/if}
									{/if}
								</div>
							{/if}
						</span>
					</Table>
				</div>
			</div>
		</div>
	</div>
</div>
