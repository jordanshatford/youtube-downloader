<script lang="ts">
	import type { DownloadState, DownloadStatus } from '@yd/client';
	import type { BadgeVariants } from '@yd/ui';
	import { Badge, ProgressBar } from '@yd/ui';

	interface Props {
		status: DownloadStatus;
	}

	let { status }: Props = $props();

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

	let text = $derived(
		status.postprocessor
			? (postProcessorLookup[status.postprocessor?.toLowerCase()] ?? status.state)
			: status.state
	);
</script>

{#key status.state}
	<Badge icon {...lookup[status.state]}>
		{text}
		{#if status.progress}
			<ProgressBar class="mt-2 -mr-2 -ml-7" value={status.progress} />
		{/if}
	</Badge>
{/key}
