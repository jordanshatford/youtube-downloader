<script lang="ts">
	import type { Snippet } from 'svelte';

	interface Props {
		children?: Snippet;
	}

	let { children }: Props = $props();
</script>

<div class="my-1 w-full px-1 md:w-1/2 lg:my-4 lg:w-1/3 lg:px-4">
	<article
		class="overflow-hidden rounded-lg border border-zinc-200 shadow dark:border-zinc-800 dark:bg-zinc-800 dark:shadow-dark"
	>
		{@render children?.()}
	</article>
</div>
