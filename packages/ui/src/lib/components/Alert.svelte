<script lang="ts">
	import type { Variant } from '$lib/types';
	import { variantMapping } from '$lib/utilities';

	export let variant: Variant = 'default';
	export let title: string;
	export let message: string | undefined = undefined;
</script>

<div
	class="{variantMapping[variant]
		.class} shadow dark:shadow-dark rounded-lg md:flex justify-between items-center top-0 py-2 px-2"
>
	<div class="sm:flex items-center">
		<div class="flex items-end">
			{#if variantMapping[variant].icon}
				<svelte:component
					this={variantMapping[variant].icon}
					size="1.5x"
					class={variantMapping[variant].class}
				/>
			{/if}
			<p class="mx-2 font-bold {variantMapping[variant].class}">{title}</p>
		</div>
		{#if message}
			<p class="pl-2 md:pl-0">{message}</p>
		{/if}
	</div>
</div>
