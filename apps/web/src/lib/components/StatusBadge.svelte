<script lang="ts">
	import { CheckCircleIcon, AlertCircleIcon, LoaderIcon } from 'svelte-feather-icons';
	import { Status } from '@yad/client';

	export let status: Status | undefined;

	let className: string;
	let icon = CheckCircleIcon;
	let iconClass = 'animate-spin';

	$: switch (status) {
		case Status.WAITING:
			className = 'bg-yellow-200 text-yellow-800';
			icon = LoaderIcon;
			iconClass = 'animate-spin';
			break;
		case Status.DOWNLOADING:
			className = 'bg-blue-200 text-blue-800';
			icon = LoaderIcon;
			iconClass = 'animate-spin';
			break;
		case Status.PROCESSING:
			className = 'bg-purple-200 text-purple-800';
			icon = LoaderIcon;
			iconClass = 'animate-spin';
			break;
		case Status.DONE:
			className = 'bg-green-200 text-green-800';
			icon = CheckCircleIcon;
			iconClass = '';
			break;
		case Status.ERROR:
			className = 'bg-red-200 text-red-800';
			icon = AlertCircleIcon;
			iconClass = '';
			break;
		default:
			status = Status.UNDEFINED;
			className = 'bg-red-200 text-red-800';
			icon = AlertCircleIcon;
			iconClass = '';
			break;
	}
</script>

<div class="h-8 w-36 rounded-lg flex items-center justify-center {className}">
	<div class="rounded-lg flex items-center justify-center h-full w-full">
		<span class="text-sm pr-2">{status}</span>
		<svelte:component this={icon} size="1x" class={iconClass} />
	</div>
</div>
