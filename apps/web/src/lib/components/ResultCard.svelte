<script lang="ts">
	import type { Video } from '@yd/client';
	import { PlusIcon, IconButton } from '@yd/ui';
	import StateIcon from '$lib/components/StateIcon.svelte';
	import { downloads } from '$lib/stores/downloads';

	export let result: Video;
</script>

<div class="my-1 w-full px-1 md:w-1/2 lg:my-4 lg:w-1/3 lg:px-4">
	<article
		class="overflow-hidden rounded-lg border border-zinc-200 shadow dark:border-zinc-800 dark:bg-zinc-800 dark:shadow-dark"
	>
		<a href={result.url} target="_blank" rel="noreferrer">
			<img alt="Thumbnail" class="block h-auto w-full" src={result.thumbnail} />
		</a>
		<header class="flex items-center justify-between p-2 leading-tight md:p-4">
			<h1 class="text-lg">
				<a
					class="text-zinc-900 no-underline hover:underline dark:text-white"
					href={result.url}
					target="_blank"
					rel="noreferrer"
				>
					{result.title}
				</a>
			</h1>
			<p class="text-sm text-zinc-700 dark:text-zinc-300">{result.duration}</p>
		</header>
		<footer class="flex items-center justify-between p-2 leading-none md:p-4">
			<a
				class="flex items-center text-zinc-800 no-underline hover:underline dark:text-zinc-400"
				href={result.channel.url}
				target="_blank"
				rel="noreferrer"
			>
				<img
					alt={result.channel.name}
					class="block h-10 w-10 rounded-lg"
					src={result.channel.thumbnail}
				/>
				<p class="ml-2 text-sm">
					{result.channel.name}
				</p>
			</a>
			{#if !(result.id in $downloads)}
				<IconButton
					on:click={() => downloads.add(result)}
					icon={PlusIcon}
					class="text-black hover:text-purple-800 dark:text-white dark:hover:text-purple-600"
					size="1.5x"
				/>
			{:else}
				<div class="p-2">
					<StateIcon state={$downloads[result.id].status.state} />
				</div>
			{/if}
		</footer>
	</article>
</div>
