<script lang="ts">
	import type { ListItem } from '$lib/utils/types';

	export let items: ListItem[];
</script>

<ol class="list-decimal py-6 md:mx-32 mx-6 text-left">
	{#each items as item}
		<li class="mt-3 text-zinc-700 dark:text-zinc-300">{item.title}</li>
		{#if item.description}
			<p class="mt-1 text-zinc-500">{item.description}</p>
		{/if}
	{/each}
</ol>
