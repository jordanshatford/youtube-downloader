<script lang="ts">
	import type { WithoutChildrenOrChild } from '$uilib/utils.js';
	import ChevronUpIcon from '@lucide/svelte/icons/chevron-up';
	import { cn } from '$uilib/utils.js';
	import { Select as SelectPrimitive } from 'bits-ui';

	let {
		ref = $bindable(null),
		class: className,
		...restProps
	}: WithoutChildrenOrChild<SelectPrimitive.ScrollUpButtonProps> = $props();
</script>

<SelectPrimitive.ScrollUpButton
	bind:ref
	data-slot="select-scroll-up-button"
	class={cn(
		"bg-popover top-0 z-10 flex w-full cursor-default items-center justify-center py-1 [&_svg:not([class*='size-'])]:size-4",
		className
	)}
	{...restProps}
>
	<ChevronUpIcon />
</SelectPrimitive.ScrollUpButton>
