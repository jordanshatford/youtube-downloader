<script lang="ts">
	import { DownloadState } from '@yd/client';
	import StateIcon from '$lib/components/StateIcon.svelte';

	export let state: DownloadState = DownloadState.ERROR;

	let className: string;

	$: switch (state) {
		case DownloadState.WAITING:
			className = 'bg-yellow-200 text-yellow-800';
			break;
		case DownloadState.DOWNLOADING:
			className = 'bg-blue-200 text-blue-800';
			break;
		case DownloadState.PROCESSING:
			className = 'bg-purple-200 text-purple-800';
			break;
		case DownloadState.DONE:
			className = 'bg-green-200 text-green-800';
			break;
		case DownloadState.ERROR:
			className = 'bg-red-200 text-red-800';
			break;
	}
</script>

<div class="flex h-8 w-36 items-center justify-center rounded-lg {className}">
	<div class="flex h-full w-full items-center justify-center rounded-lg">
		<span class="pr-2 text-sm">{state}</span>
		<StateIcon {state} size="1x" />
	</div>
</div>
