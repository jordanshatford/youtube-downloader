<script lang="ts">
	import AppDownloadStatusIcon from '$lib/components/app-download-status-icon.svelte';
	import { downloads } from '$lib/stores/downloads.svelte';

	import type { Video } from '@yd/client';
	import { Button, Item, PlusIcon } from '@yd/ui';

	interface Props {
		result: Video;
	}

	let { result }: Props = $props();
</script>

<Item.Root variant="outline">
	<Item.Media variant="image" class="w-20">
		<a href={result.url} target="_blank" rel="noreferrer external">
			<img alt="Thumbnail" class="aspect-video" src={result.thumbnail} />
		</a>
	</Item.Media>
	<Item.Content>
		<Item.Title>
			<a class="line-clamp-2" href={result.url} target="_blank" rel="noreferrer external">
				{result.title}
			</a></Item.Title
		>
		<Item.Description>
			<a class="no-underline!" href={result.channel.url} target="_blank" rel="noreferrer external">
				{result.channel.name}
			</a></Item.Description
		>
	</Item.Content>
	<Item.Content>
		<Item.Description>{result.duration}</Item.Description>
	</Item.Content>
	<Item.Actions>
		{#if !(result.id in downloads.downloads)}
			<Button.Root variant="outline" size="icon" onclick={() => downloads.add(result)}>
				<PlusIcon />
			</Button.Root>
		{:else}
			<AppDownloadStatusIcon status={downloads.downloads[result.id].status} />
		{/if}
	</Item.Actions>
</Item.Root>
