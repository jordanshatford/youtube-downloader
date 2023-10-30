<script lang="ts">
	import { DownloadState } from '@yd/client';
	import { ActionIcon, ArrowPathIcon, ButtonGroup, Confirm, DownloadIcon, TrashIcon } from '@yd/ui';
	import { downloads, type DownloadWithExtra } from '$lib/stores/downloads';

	export let download: DownloadWithExtra;
</script>

<ButtonGroup>
	<ActionIcon
		title="Get Download File"
		src={DownloadIcon}
		loading={download.awaitingFileBlob}
		disabled={download.status?.state !== DownloadState.DONE}
		on:click={async () => await downloads.getFile(download.video.id)}
	/>
	<ActionIcon
		title="Retry Download"
		src={ArrowPathIcon}
		disabled={download.status?.state !== DownloadState.ERROR}
		on:click={async () => await downloads.restart(download.video.id)}
	/>
	<Confirm
		variant="error"
		title="Delete download?"
		description="Are you sure you want to delete this download? Deleting is permanent."
		cancelText="Cancel"
		confirmText="Delete"
		let:confirm={onConfirm}
	>
		<ActionIcon
			title="Delete Download"
			src={TrashIcon}
			disabled={download.status?.state !== DownloadState.DONE &&
				download.status?.state !== DownloadState.ERROR}
			on:click={() => onConfirm(() => downloads.remove(download.video.id))}
		/>
	</Confirm>
</ButtonGroup>
