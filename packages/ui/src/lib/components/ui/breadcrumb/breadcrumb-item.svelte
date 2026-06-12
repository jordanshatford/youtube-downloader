<script lang="ts">
	import type { WithElementRef } from '$uilib/utils.js';
	import type { HTMLLiAttributes } from 'svelte/elements';
	import { cn } from '$uilib/utils.js';

	let {
		ref = $bindable(null),
		class: className,
		children,
		...restProps
	}: WithElementRef<HTMLLiAttributes> = $props();
</script>

<li
	bind:this={ref}
	data-slot="breadcrumb-item"
	class={cn('gap-1.5 inline-flex items-center', className)}
	{...restProps}
>
	{@render children?.()}
</li>
