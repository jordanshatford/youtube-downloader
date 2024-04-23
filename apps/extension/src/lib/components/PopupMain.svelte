<script lang="ts">
	import { onMount } from 'svelte';

	import { Badge, Button, Card, IconButton, PlusIcon } from '@yd/ui';

	import type { Ctx } from '~/lib/context-service';
	import DownloadActions from '~/lib/components/DownloadActions.svelte';
	import PopupError from '~/lib/components/PopupError.svelte';
	import StateIcon from '~/lib/components/StateIcon.svelte';
	import StatusBadge from '~/lib/components/StatusBadge.svelte';
	import { createContextStore } from '~/lib/stores/context';

	export let ctx: Ctx;

	const store = createContextStore(ctx);

	onMount(store.onMount);
</script>

{#if $store.video}
	{@const options = $store.currentDownload ? $store.currentDownload.options : $store.options}
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
			{#if !$store.currentDownload}
				<IconButton
					on:click={async () => await store.download()}
					src={PlusIcon}
					class="h-8 w-8 p-1 text-black hover:text-brand-600 dark:text-white dark:hover:text-brand-600"
				/>
			{:else}
				<StateIcon state={$store.currentDownload.status.state} />
			{/if}
		</footer>
	</Card>
	<Card>
		<div class="flex max-w-full flex-wrap justify-center gap-2 p-2">
			<Badge icon={false} variant="success">{options.format.toUpperCase()}</Badge>
			<Badge icon={false} variant="success">{options.quality.toUpperCase()}</Badge>
			<Badge icon={false} variant={options.embed_metadata ? 'success' : 'error'}>Metadata</Badge>
			<Badge icon={false} variant={options.embed_thumbnail ? 'success' : 'error'}>Thumbnail</Badge>
			<Badge icon={false} variant={options.embed_subtitles ? 'success' : 'error'}>Subtitles</Badge>
		</div>
	</Card>
	<div class="flex max-w-full flex-wrap justify-center gap-2 p-2">
		{#if $store.currentDownload}
			{#if ['DONE', 'ERROR'].includes($store.currentDownload.status.state)}
				<DownloadActions download={$store.currentDownload} {store} />
			{:else}
				<StatusBadge status={$store.currentDownload.status} />
			{/if}
		{:else}
			<Button disabled={$store.video === undefined} on:click={async () => await store.download()}>
				Download
			</Button>
		{/if}
	</div>
{:else}
	<PopupError message="Page does not contain a valid YouTube video." />
{/if}
