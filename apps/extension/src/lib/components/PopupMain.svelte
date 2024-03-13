<script lang="ts">
	import { onMount } from 'svelte';
	import { Card, Button, Badge } from '@yd/ui';
	import type { Ctx } from '~/lib/context-service';
	import StatusBadge from '~/lib/components/StatusBadge.svelte';
	import { createContextStore } from '~/lib/stores/context';
	import PopupError from '~/lib/components/PopupError.svelte';

	export let ctx: Ctx;

	const store = createContextStore(ctx);

	onMount(store.onMount);
</script>

{#if $store.video}
	<Card>
		<img alt="Thumbnail" class="block h-auto w-full" src={$store.video?.thumbnail} />
		<header class="flex items-center justify-between p-2 leading-tight md:p-4">
			<h1 class="line-clamp-2 text-lg text-zinc-900 dark:text-white">
				{$store.video?.title}
			</h1>
			<p class="text-sm text-zinc-700 dark:text-zinc-300">{$store.video?.duration}</p>
		</header>
		<footer class="flex items-center justify-between p-2 leading-none md:p-4">
			<div class="flex items-center text-zinc-800 dark:text-zinc-400">
				<img
					alt={$store.video?.channel.name}
					class="block h-10 w-10 rounded-lg"
					src={$store.video?.channel.thumbnail}
				/>
				<p class="ml-2 text-sm">
					{$store.video?.channel.name}
				</p>
			</div>
		</footer>
	</Card>
	<div class="flex max-w-full flex-wrap justify-center gap-2">
		<Badge>{$store.options.format.toUpperCase()}</Badge>
		<Badge>{$store.options.quality.toUpperCase()}</Badge>
		{#if $store.options.embed_metadata}
			<Badge>Metadata</Badge>
		{/if}
		{#if $store.options.embed_thumbnail}
			<Badge>Thumbnail</Badge>
		{/if}
		{#if $store.options.embed_subtitles}
			<Badge>Subtitles</Badge>
		{/if}
	</div>
	{#if $store.currentDownload}
		<StatusBadge status={$store.currentDownload.status} />
	{:else}
		<Button disabled={$store.video === undefined} on:click={async () => await store.download()}>
			Download
		</Button>
	{/if}
{:else}
	<PopupError message="Page does not contain a valid YouTube video." />
{/if}
