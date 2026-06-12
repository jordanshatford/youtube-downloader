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
	data-slot="sheet-header"
	class={cn('gap-1.5 p-4 flex flex-col', className)}
	{...restProps}
>
	{@render children?.()}
</div>
