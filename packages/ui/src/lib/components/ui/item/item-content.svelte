<script lang="ts">
	import type { WithElementRef } from '$uilib/utils.js';
	import type { HTMLAttributes } from 'svelte/elements';
	import { cn } from '$uilib/utils.js';

	let {
		ref = $bindable(null),
		class: className,
		children,
		...restProps
	}: WithElementRef<HTMLAttributes<HTMLDivElement>> = $props();
</script>

<div
	bind:this={ref}
	data-slot="item-content"
	class={cn(
		'flex flex-1 flex-col gap-1 group-data-[size=xs]/item:gap-0 [&+[data-slot=item-content]]:flex-none',
		className
	)}
	{...restProps}
>
	{@render children?.()}
</div>
