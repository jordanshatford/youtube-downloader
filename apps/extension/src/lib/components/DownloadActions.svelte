<script lang="ts">
	import type { Download } from '@yd/client';
	import { ActionIcon, ArrowPathIcon, ButtonGroup, Confirm, DownloadIcon, TrashIcon } from '@yd/ui';

	import { createContextStore } from '~/lib/stores/context';

	export let store: ReturnType<typeof createContextStore>;
	export let download: Download;

	let isWaitingForBlob = false;

	async function getDownloadFile() {
		isWaitingForBlob = true;
		await store.getFile(download.video.id);
		isWaitingForBlob = false;
	}
</script>

<ButtonGroup>
	<ActionIcon
		title="Get Download File"
		src={DownloadIcon}
		loading={isWaitingForBlob}
		disabled={download.status.state !== 'DONE'}
		on:click={async () => await getDownloadFile()}
	/>
	<ActionIcon
		title="Retry Download"
		src={ArrowPathIcon}
		disabled={download.status.state !== 'ERROR'}
		on:click={async () => await store.restart(download.video.id)}
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
			disabled={!['DONE', 'ERROR'].includes(download.status.state)}
			on:click={() => onConfirm(() => store.remove(download.video.id))}
		/>
	</Confirm>
</ButtonGroup>
