<script lang="ts">
	import type { Snippet } from 'svelte';

	interface Props {
		children?: Snippet;
	}

	let { children }: Props = $props();
</script>

<span
	class="inline-flex divide-x overflow-hidden rounded-lg border bg-white shadow-xs dark:divide-zinc-800 dark:border-zinc-800 dark:bg-zinc-900"
>
	{@render children?.()}
</span>
