<script lang="ts">
	import { DownloadState } from '@yd/client';
	import {
		CheckCircleIcon,
		LoaderIcon,
		ExclamationCircleIcon,
		Icon,
		type IconSource
	} from '@yd/ui';

	export let state: DownloadState;

	const lookup: Record<DownloadState, { icon: IconSource; class: string }> = {
		[DownloadState.WAITING]: {
			icon: LoaderIcon,
			class: 'text-yellow-600 animate-spin'
		},
		[DownloadState.DOWNLOADING]: {
			icon: LoaderIcon,
			class: 'text-blue-600 animate-spin'
		},
		[DownloadState.PROCESSING]: {
			icon: LoaderIcon,
			class: 'text-blue-600 animate-spin'
		},
		[DownloadState.ERROR]: {
			icon: ExclamationCircleIcon,
			class: 'text-red-600'
		},
		[DownloadState.DONE]: {
			icon: CheckCircleIcon,
			class: 'text-green-600'
		}
	};
</script>

{#key state}
	<Icon src={lookup[state].icon} theme="solid" class="h-5 w-5 {lookup[state].class}" />
{/key}
