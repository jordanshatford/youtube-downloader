<script lang="ts">
	import { CheckCircleIcon, LoaderIcon, AlertCircleIcon } from 'svelte-feather-icons';
	import { Status } from '$lib/utils/types';

	export let status: Status;
	let className = 'animate-spin';
	let icon = LoaderIcon;

	$: switch (status) {
		case Status.WAITING:
			className = 'text-yellow-600 animate-spin';
			icon = LoaderIcon;
			break;
		case Status.DOWNLOADING:
			className = 'text-blue-600 animate-spin';
			icon = LoaderIcon;
			break;
		case Status.PROCESSING:
			className = 'text-purple-600 animate-spin';
			icon = LoaderIcon;
			break;
		case Status.DONE:
			className = 'text-green-600';
			icon = CheckCircleIcon;
			break;
		case Status.ERROR:
		default:
			className = 'text-red-600';
			icon = AlertCircleIcon;
			break;
	}
</script>

<div class="p-2">
	<svelte:component this={icon} class={className} size="1.5x" />
</div>
