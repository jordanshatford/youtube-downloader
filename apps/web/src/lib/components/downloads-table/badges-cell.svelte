<script lang="ts">
	import type { HTMLAttributes } from 'svelte/elements';

	import { Badge, cn } from '@yd/ui';

	let {
		items,
		class: className,
		...restProps
	}: {
		items: string[];
	} & HTMLAttributes<HTMLDivElement> = $props();
</script>

<div class={cn('flex flex-wrap gap-2', className)} {...restProps}>
	{#each items as item (item)}
		<Badge variant="secondary">{item}</Badge>
	{/each}
</div>
