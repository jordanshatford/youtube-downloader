<script lang="ts">
	import type { ComponentProps } from 'svelte';
	import { downloads } from '$lib/stores/downloads.svelte';

	import type { Download } from '@yd/client';
	import type { Row } from '@yd/ui';
	import {
		AlertDialog,
		Button,
		DropdownMenu,
		EllipsisIcon,
		FileDownloadIcon,
		RotateIcon,
		TrashIcon
	} from '@yd/ui';

	let {
		rows,
		...restProps
	}: { rows: Row<Download>[] } & ComponentProps<typeof DropdownMenu.Trigger> = $props();

	let downloadableRows = $derived(rows.filter((r) => r.original.status.state === 'DONE'));
	let isDownloadDisabled = $derived(downloadableRows.length === 0);
	let retryableRows = $derived(rows.filter((r) => r.original.status.state === 'ERROR'));
	let isRetryDisabled = $derived(retryableRows.length === 0);
	let deletableRows = $derived(
		rows.filter((r) => ['DONE', 'ERROR'].includes(r.original.status.state))
	);
	let isDeleteDisabled = $derived(deletableRows.length === 0);

	let isWaitingForFileDownload = $state(false);
	let isDeleteAlertDialogOpen = $state(false);

	async function handleDownloadFile() {
		isWaitingForFileDownload = true;
		const promises = downloadableRows.map((r) => downloads.getFile(r.original.video.id));
		await Promise.all(promises);
		isWaitingForFileDownload = false;
	}

	async function handleRetry() {
		const promises = retryableRows.map((r) => downloads.restart(r.original.video.id));
		await Promise.all(promises);
	}

	function handleDeleteAlertDialog(e: Event) {
		e.preventDefault();
		isDeleteAlertDialogOpen = true;
	}

	async function handleDelete() {
		const promises = deletableRows.map((r) => downloads.remove(r.original.video.id));
		await Promise.all(promises);
		isDeleteAlertDialogOpen = false;
	}
</script>

<DropdownMenu.Root>
	<DropdownMenu.Trigger {...restProps} disabled={isWaitingForFileDownload}>
		{#snippet child({ props })}
			<Button.Root {...props} variant="ghost" class="data-[state=open]:bg-muted flex h-8 w-8 p-0">
				<EllipsisIcon />
				<span class="sr-only">Open Menu</span>
			</Button.Root>
		{/snippet}
	</DropdownMenu.Trigger>
	<DropdownMenu.Content class="w-44" align="end">
		<DropdownMenu.Label>Actions</DropdownMenu.Label>
		<DropdownMenu.Separator />
		<DropdownMenu.Item disabled={isDownloadDisabled} onclick={handleDownloadFile}>
			<FileDownloadIcon />{downloadableRows.length > 1
				? `Download Files (${downloadableRows.length})`
				: 'Download File'}
		</DropdownMenu.Item>
		<DropdownMenu.Item disabled={isRetryDisabled} onclick={handleRetry}>
			<RotateIcon />{retryableRows.length > 1 ? `Retry (${retryableRows.length})` : 'Retry'}
		</DropdownMenu.Item>
		<DropdownMenu.Separator />
		<DropdownMenu.Item disabled={isDeleteDisabled} onclick={handleDeleteAlertDialog}>
			<TrashIcon />{deletableRows.length > 1 ? `Delete (${deletableRows.length})` : 'Delete'}
		</DropdownMenu.Item>
	</DropdownMenu.Content>
</DropdownMenu.Root>

<AlertDialog.Root bind:open={isDeleteAlertDialogOpen}>
	<AlertDialog.Content>
		<AlertDialog.Header>
			<AlertDialog.Title>Delete download?</AlertDialog.Title>
			<AlertDialog.Description>
				Are you sure you want to delete this download? Deleting is permanent.
			</AlertDialog.Description>
		</AlertDialog.Header>
		<AlertDialog.Footer>
			<AlertDialog.Cancel>Cancel</AlertDialog.Cancel>
			<AlertDialog.Action onclick={handleDelete}>Delete</AlertDialog.Action>
		</AlertDialog.Footer>
	</AlertDialog.Content>
</AlertDialog.Root>
