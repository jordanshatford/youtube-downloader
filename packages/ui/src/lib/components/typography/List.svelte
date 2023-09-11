<script lang="ts">
	export let items: { title: string; description?: string }[];
</script>

<ol class="mx-6 list-decimal py-6 text-left md:mx-32">
	{#each items as item}
		<li class="mt-3 text-zinc-700 dark:text-zinc-300">{item.title}</li>
		{#if item.description}
			<p class="mt-1 text-zinc-500">{item.description}</p>
		{/if}
	{/each}
</ol>
