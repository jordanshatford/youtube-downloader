<script lang="ts">
	import StatusButton from '$lib/components/StatusButton.svelte';
	import { PlusIcon } from 'svelte-feather-icons';
	import IconButton from '$lib/components/ui/IconButton.svelte';
	import { downloads } from '$lib/stores/downloads';
	import type { VideoInfo } from '$lib/utils/types';
	import { Status } from '$lib/utils/types';

	export let result: VideoInfo;
</script>

<div class="my-1 px-1 w-full md:w-1/2 lg:my-4 lg:px-4 lg:w-1/3">
	<article
		class="rounded-lg dark:bg-zinc-800 overflow-hidden shadow dark:shadow-dark border border-zinc-200 dark:border-zinc-800"
	>
		<a href={result.url} target="_blank" rel="noreferrer">
			<img alt="Thumbnail" class="block h-auto w-full" src={result.thumbnail} />
		</a>
		<header class="flex items-center justify-between leading-tight p-2 md:p-4">
			<h1 class="text-lg">
				<a
					class="no-underline hover:underline text-zinc-900 dark:text-white"
					href={result.url}
					target="_blank"
					rel="noreferrer"
				>
					{result.title}
				</a>
			</h1>
			<p class="text-zinc-700 dark:text-zinc-300 text-sm">{result.duration ?? '???'}</p>
		</header>
		<footer class="flex items-center justify-between leading-none p-2 md:p-4">
			<a
				class="flex items-center no-underline hover:underline text-zinc-800 dark:text-zinc-400"
				href={result.channel.url}
				target="_blank"
				rel="noreferrer"
			>
				<img
					alt={result.channel.name}
					class="block w-10 h-10 rounded-lg"
					src={result.channel.thumbnail}
				/>
				<p class="ml-2 text-sm">
					{result.channel.name}
				</p>
			</a>
			{#if !(result.id in $downloads)}
				<IconButton
					on:click={() => downloads.add({ ...result, status: Status.WAITING })}
					icon={PlusIcon}
					class="text-black dark:text-white hover:text-purple-800 dark:hover:text-purple-600"
					size="1.5x"
				/>
			{:else}
				<StatusButton status={$downloads[result.id]?.status} />
			{/if}
		</footer>
	</article>
</div>
