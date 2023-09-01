<script lang="ts">
	import { CheckCircleIcon, LoaderIcon, AlertCircleIcon } from 'svelte-feather-icons';
	import { DownloadState } from '@yd/client';

	export let state: DownloadState;
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
		default:
			className = 'text-red-600';
			icon = AlertCircleIcon;
			break;
	}
</script>

<div class="p-2">
	<svelte:component this={icon} class={className} size="1.5x" />
</div>
