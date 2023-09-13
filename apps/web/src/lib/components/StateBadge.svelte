<script lang="ts">
	import { DownloadState } from '@yd/client';
	import { Badge, type BadgeVariants } from '@yd/ui';

	export let state: DownloadState = DownloadState.ERROR;

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
</script>

<div class="flex h-8 w-36 items-center justify-start">
	{#key state}
		<Badge icon {...lookup[state]}>{state}</Badge>
	{/key}
</div>
