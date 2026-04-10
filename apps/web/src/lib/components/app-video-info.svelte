<script lang="ts">
	import type { ComponentProps } from 'svelte';

	import type { Video } from '@yd/client';
	import { cn, Item } from '@yd/ui';

	interface Props {
		video: Video;
	}

	let {
		video,
		class: className,
		...restProps
	}: Props & ComponentProps<typeof Item.Root> = $props();
</script>

<Item.Root {...restProps} class={cn('p-1', className)}>
	<Item.Media variant="default" class="hidden aspect-video h-10 md:flex">
		<a href={video.url} target="_blank" rel="noreferrer external">
			<img alt="Thumbnail" class="" src={video.thumbnail} />
		</a>
	</Item.Media>
	<Item.Content>
		<Item.Title>
			<a class="line-clamp-2" href={video.url} target="_blank" rel="noreferrer external">
				{video.title}
			</a></Item.Title
		>
		<Item.Description>
			<a class="no-underline!" href={video.channel.url} target="_blank" rel="noreferrer external">
				{video.channel.name}
			</a></Item.Description
		>
	</Item.Content>
</Item.Root>
