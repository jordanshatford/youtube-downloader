<script lang="ts">
	import type { Variant } from '../types';
	import { variantMapping } from '../utilities';
	import { Icon } from '../icons';

	export let variant: Variant = 'default';
	export let title: string;
	export let message: string | undefined = undefined;
</script>

<div
	class="{variantMapping[variant]
		.class} top-0 items-center justify-between rounded-lg px-2 py-2 shadow dark:shadow-dark md:flex"
>
	<div class="items-center sm:flex">
		<div class="flex items-end">
			{#if variantMapping[variant].icon}
				<Icon src={variantMapping[variant].icon} class="h-5 w-5 {variantMapping[variant].class}" />
			{/if}
			<p class="mx-2 font-bold {variantMapping[variant].class}">{title}</p>
		</div>
		{#if message}
			<p class="pl-2 md:pl-0">{message}</p>
		{/if}
	</div>
</div>
