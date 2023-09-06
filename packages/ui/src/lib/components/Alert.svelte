<script lang="ts">
	import { CheckCircleIcon, AlertTriangleIcon, AlertCircleIcon, InfoIcon } from '../icons';
	import type { Variant } from '../types';

	export let variant: Variant = 'default';
	export let title: string;
	export let message: string | null = null;

	const themes = {
		error: {
			icon: AlertCircleIcon,
			class: 'text-red-800 bg-red-200'
		},
		success: {
			icon: CheckCircleIcon,
			class: 'text-green-700 bg-green-200'
		},
		warning: {
			icon: AlertTriangleIcon,
			class: 'text-yellow-600 bg-yellow-200'
		},
		info: {
			icon: InfoIcon,
			class: 'text-blue-800 bg-blue-200'
		},
		default: {
			icon: undefined,
			class: 'bg-zinc-400 text-zinc-800'
		}
	};
</script>

<div
	class="{themes[variant]
		.class} shadow dark:shadow-dark rounded-lg md:flex justify-between items-center top-0 py-2 px-2"
>
	<div class="sm:flex items-center">
		<div class="flex items-end">
			{#if themes[variant].icon}
				<svelte:component this={themes[variant].icon} size="1.5x" class={themes[variant].class} />
			{/if}
			<p class="mx-2 font-bold {themes[variant].class}">{title}</p>
		</div>
		{#if message}
			<p class="pl-2 md:pl-0">{message}</p>
		{/if}
	</div>
</div>
