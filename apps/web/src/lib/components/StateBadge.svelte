<script lang="ts">
	import { CheckCircleIcon, AlertCircleIcon, LoaderIcon } from 'svelte-feather-icons';
	import { DownloadState } from '@yd/client';

	export let state: DownloadState = DownloadState.ERROR;

	let className: string;
	let icon = CheckCircleIcon;
	let iconClass = 'animate-spin';

	$: switch (state) {
		case DownloadState.WAITING:
			className = 'bg-yellow-200 text-yellow-800';
			icon = LoaderIcon;
			iconClass = 'animate-spin';
			break;
		case DownloadState.DOWNLOADING:
			className = 'bg-blue-200 text-blue-800';
			icon = LoaderIcon;
			iconClass = 'animate-spin';
			break;
		case DownloadState.PROCESSING:
			className = 'bg-purple-200 text-purple-800';
			icon = LoaderIcon;
			iconClass = 'animate-spin';
			break;
		case DownloadState.DONE:
			className = 'bg-green-200 text-green-800';
			icon = CheckCircleIcon;
			iconClass = '';
			break;
		case DownloadState.ERROR:
			className = 'bg-red-200 text-red-800';
			icon = AlertCircleIcon;
			iconClass = '';
			break;
	}
</script>

<div class="h-8 w-36 rounded-lg flex items-center justify-center {className}">
	<div class="rounded-lg flex items-center justify-center h-full w-full">
		<span class="text-sm pr-2">{state}</span>
		<svelte:component this={icon} size="1x" class={iconClass} />
	</div>
</div>
