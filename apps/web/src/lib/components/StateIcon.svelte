<script lang="ts">
	import type { DownloadState } from '@yd/client';
	import type { IconSource } from '@yd/ui';
	import { CheckCircleIcon, ExclamationCircleIcon, Icon, LoaderIcon } from '@yd/ui';

	interface Props {
		state: DownloadState;
	}

	let { state }: Props = $props();

	const lookup: Record<DownloadState, { icon: IconSource; class: string }> = {
		WAITING: {
			icon: LoaderIcon,
			class: 'bg-yellow-100 text-yellow-700 dark:bg-yellow-700 dark:text-yellow-100 animate-spin'
		},
		DOWNLOADING: {
			icon: LoaderIcon,
			class: 'bg-blue-100 text-blue-700 dark:bg-blue-700 dark:text-blue-100 animate-spin'
		},
		PROCESSING: {
			icon: LoaderIcon,
			class: 'bg-blue-100 text-blue-700 dark:bg-blue-700 dark:text-blue-100 animate-spin'
		},
		ERROR: {
			icon: ExclamationCircleIcon,
			class: 'bg-red-100 text-red-700 dark:bg-red-700 dark:text-red-100'
		},
		DONE: {
			icon: CheckCircleIcon,
			class: 'bg-emerald-100 text-emerald-700 dark:bg-emerald-700 dark:text-emerald-100'
		}
	};
</script>

{#key state}
	<Icon
		src={lookup[state].icon}
		theme="solid"
		class="h-8 w-8 rounded-full p-1 {lookup[state].class}"
	/>
{/key}
