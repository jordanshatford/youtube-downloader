<script lang="ts">
	import { DownloadState } from '@yd/client';
	import { ActionIcon, ArrowPathIcon, ButtonGroup, Confirm, DownloadIcon, TrashIcon } from '@yd/ui';
	import { downloads, type VideoWithExtra } from '$lib/stores/downloads';

	export let video: VideoWithExtra;
</script>

<ButtonGroup>
	<ActionIcon
		title="Get Download File"
		src={DownloadIcon}
		loading={video.awaitingFileBlob}
		disabled={video.status.state !== DownloadState.DONE}
		on:click={async () => await downloads.getFile(video.id)}
	/>
	<ActionIcon
		title="Retry Download"
		src={ArrowPathIcon}
		disabled={video.status.state !== DownloadState.ERROR}
		on:click={async () => await downloads.restart(video.id)}
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
			disabled={![DownloadState.DONE, DownloadState.ERROR].includes(video.status.state)}
			on:click={() => onConfirm(() => downloads.remove(video.id))}
		/>
	</Confirm>
</ButtonGroup>
