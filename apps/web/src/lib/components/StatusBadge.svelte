<script lang="ts">
	import { DownloadState, type DownloadStatus } from '@yd/client';
	import { Badge, type BadgeVariants, ProgressBar } from '@yd/ui';

	export let status: DownloadStatus = {
		state: DownloadState.ERROR
	};

	const postProcessorLookup: Record<string, string> = {
		extractaudio: 'EXTRACTING AUDIO',
		videoconvertor: 'CONVERTING VIDEO',
		metadata: 'EMBEDDING',
		embedthumbnail: 'EMBEDDING',
		embedsubtitle: 'EMBEDDING',
		movefiles: 'FINALIZING'
	};

	const lookup: Record<DownloadState, BadgeVariants> = {
		[DownloadState.WAITING]: {
			variant: 'warning',
			loading: true
		},
		[DownloadState.DOWNLOADING]: {
			variant: 'info',
			loading: true
		},
		[DownloadState.PROCESSING]: {
			variant: 'info',
			loading: true
		},
		[DownloadState.ERROR]: {
			variant: 'error'
		},
		[DownloadState.DONE]: {
			variant: 'success'
		}
	};

	$: text = status.postprocessor
		? postProcessorLookup[status.postprocessor?.toLowerCase()] ?? status.state
		: status.state;
</script>

{#key status}
	<Badge icon {...lookup[status.state]}>
		{text}
		{#if status.progress}
			<ProgressBar class="-ml-7 -mr-2 mt-2" value={status.progress} />
		{/if}
	</Badge>
{/key}
