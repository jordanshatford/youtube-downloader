<script lang="ts">
	import type { WithoutChild } from '$uilib/utils.js';
	import { cn } from '$uilib/utils.js';
	import { Accordion as AccordionPrimitive } from 'bits-ui';

	let {
		ref = $bindable(null),
		class: className,
		children,
		...restProps
	}: WithoutChild<AccordionPrimitive.ContentProps> = $props();
</script>

<AccordionPrimitive.Content
	bind:ref
	data-slot="accordion-content"
	class="data-open:animate-accordion-down data-closed:animate-accordion-up overflow-hidden text-sm"
	{...restProps}
>
	<div
		class={cn(
			'[&_a]:hover:text-foreground pt-0 pb-4 [&_a]:underline [&_a]:underline-offset-3 [&_p:not(:last-child)]:mb-4',
			className
		)}
	>
		{@render children?.()}
	</div>
</AccordionPrimitive.Content>
