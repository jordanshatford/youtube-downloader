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

	let { row, ...restProps }: { row: Row<Download> } & ComponentProps<typeof DropdownMenu.Trigger> =
		$props();

	let isWaitingBlob = $state(false);
	let open = $state(false);

	async function getDownloadFile() {
		isWaitingBlob = true;
		await downloads.getFile(row.original.video.id);
		isWaitingBlob = false;
	}

	function handleDeleteClick(e: Event) {
		e.preventDefault();
		open = true;
	}
</script>

<DropdownMenu.Root>
	<DropdownMenu.Trigger {...restProps} disabled={isWaitingBlob}>
		{#snippet child({ props })}
			<Button.Root {...props} variant="ghost" class="data-[state=open]:bg-muted flex h-8 w-8 p-0">
				<EllipsisIcon />
				<span class="sr-only">Open Menu</span>
			</Button.Root>
		{/snippet}
	</DropdownMenu.Trigger>
	<DropdownMenu.Content class="w-40" align="end">
		<DropdownMenu.Item
			disabled={row.original.status.state !== 'DONE'}
			onclick={async () => await getDownloadFile()}
			><FileDownloadIcon />Download File</DropdownMenu.Item
		>
		<DropdownMenu.Item
			disabled={row.original.status.state !== 'ERROR'}
			onclick={async () => await downloads.restart(row.original.video.id)}
			><RotateIcon />Retry</DropdownMenu.Item
		>
		<DropdownMenu.Separator />
		<DropdownMenu.Item
			disabled={!['DONE', 'ERROR'].includes(row.original.status.state)}
			onclick={handleDeleteClick}
		>
			<TrashIcon />Delete
		</DropdownMenu.Item>
	</DropdownMenu.Content>
</DropdownMenu.Root>

<AlertDialog.Root bind:open>
	<AlertDialog.Content>
		<AlertDialog.Header>
			<AlertDialog.Title>Delete download?</AlertDialog.Title>
			<AlertDialog.Description>
				Are you sure you want to delete this download? Deleting is permanent.
			</AlertDialog.Description>
		</AlertDialog.Header>
		<AlertDialog.Footer>
			<AlertDialog.Cancel>Cancel</AlertDialog.Cancel>
			<AlertDialog.Action
				onclick={async () => {
					await downloads.remove(row.original.video.id);
					open = false;
				}}>Delete</AlertDialog.Action
			>
		</AlertDialog.Footer>
	</AlertDialog.Content>
</AlertDialog.Root>
