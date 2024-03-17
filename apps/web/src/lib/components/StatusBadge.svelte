<script lang="ts">
	import type { DownloadState, DownloadStatus } from '@yd/client';
	import { Badge, type BadgeVariants, ProgressBar } from '@yd/ui';

	export let status: DownloadStatus;

	const postProcessorLookup: Record<string, string> = {
		extractaudio: 'EXTRACTING AUDIO',
		videoconvertor: 'CONVERTING VIDEO',
		metadata: 'EMBEDDING',
		embedthumbnail: 'EMBEDDING',
		embedsubtitle: 'EMBEDDING',
		movefiles: 'FINALIZING'
	};

	const lookup: Record<DownloadState, BadgeVariants> = {
		WAITING: {
			variant: 'warning',
			loading: true
		},
		DOWNLOADING: {
			variant: 'info',
			loading: true
		},
		PROCESSING: {
			variant: 'info',
			loading: true
		},
		ERROR: {
			variant: 'error'
		},
		DONE: {
			variant: 'success'
		}
	};

	$: text = status.postprocessor
		? postProcessorLookup[status.postprocessor?.toLowerCase()] ?? status.state
		: status.state;
</script>

{#key status.state}
	<Badge icon {...lookup[status.state]}>
		{text}
		{#if status.progress}
			<ProgressBar class="-ml-7 -mr-2 mt-2" value={status.progress} />
		{/if}
	</Badge>
{/key}
