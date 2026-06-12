<script lang="ts">
	import { cn } from '$uilib/utils.js';
	import { Tabs as TabsPrimitive } from 'bits-ui';

	let {
		ref = $bindable(null),
		class: className,
		...restProps
	}: TabsPrimitive.ContentProps = $props();
</script>

<TabsPrimitive.Content
	bind:ref
	data-slot="tabs-content"
	class={cn('text-sm flex-1 outline-none', className)}
	{...restProps}
/>
