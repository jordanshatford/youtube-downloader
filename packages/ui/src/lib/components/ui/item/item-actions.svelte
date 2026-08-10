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
	data-slot="item-actions"
	class={cn('flex items-center gap-2', className)}
	{...restProps}
>
	{@render children?.()}
</div>
