<script lang="ts">
	import type { Snippet } from 'svelte';

	interface Props {
		children?: Snippet;
	}

	let { children }: Props = $props();
</script>

<p
	class="mt-2 text-center text-3xl leading-8 font-extrabold tracking-tight text-zinc-900 dark:text-zinc-100"
>
	{@render children?.()}
</p>
