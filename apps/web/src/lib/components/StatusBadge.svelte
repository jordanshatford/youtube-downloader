<script lang="ts">
	import { DownloadState, type DownloadStatus } from '@yd/client';
	import { Badge, type BadgeVariants } from '@yd/ui';

	export let status: DownloadStatus = {
		state: DownloadState.ERROR
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

	$: content =
		status.state === DownloadState.DOWNLOADING
			? `${status.state} ${(status.progress ?? 0).toFixed(1)}%`
			: status.state;
</script>

<div class="flex h-8 w-36 items-center justify-start">
	{#key status}
		<Badge icon {...lookup[status.state]}>{content}</Badge>
	{/key}
</div>
