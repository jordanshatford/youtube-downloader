<script lang="ts">
	import StateIcon from '$lib/components/StateIcon.svelte';
	import { downloads } from '$lib/stores/downloads';

	import type { Video } from '@yd/client';
	import { Card, IconButton, PlusIcon } from '@yd/ui';

	interface Props {
		result: Video;
	}

	let { result }: Props = $props();
</script>

<Card>
	<a href={result.url} target="_blank" rel="noreferrer">
		<img alt="Thumbnail" class="block h-auto w-full" src={result.thumbnail} />
	</a>
	<header class="flex items-center justify-between p-2 leading-tight md:p-4">
		<h1 class="text-lg">
			<a
				class="line-clamp-2 text-zinc-900 no-underline hover:underline dark:text-white"
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
				onclick={() => downloads.add(result)}
				src={PlusIcon}
				class="h-8 w-8 p-1 text-black hover:text-brand-600 dark:text-white dark:hover:text-brand-600"
			/>
		{:else}
			<StateIcon state={$downloads[result.id].status.state} />
		{/if}
	</footer>
</Card>
