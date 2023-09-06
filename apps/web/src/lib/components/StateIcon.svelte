<script lang="ts">
	import { DownloadState } from '@yd/client';
	import { CheckCircleIcon, LoaderIcon, AlertCircleIcon } from '@yd/ui';

	export let state: DownloadState;
	export let size: string = '1.5x';
	let className = 'animate-spin';
	let icon = LoaderIcon;

	$: switch (state) {
		case DownloadState.WAITING:
			className = 'text-yellow-600 animate-spin';
			icon = LoaderIcon;
			break;
		case DownloadState.DOWNLOADING:
			className = 'text-blue-600 animate-spin';
			icon = LoaderIcon;
			break;
		case DownloadState.PROCESSING:
			className = 'text-purple-600 animate-spin';
			icon = LoaderIcon;
			break;
		case DownloadState.DONE:
			className = 'text-green-600';
			icon = CheckCircleIcon;
			break;
		case DownloadState.ERROR:
			className = 'text-red-600';
			icon = AlertCircleIcon;
			break;
	}
</script>

<svelte:component this={icon} class={className} {size} />
