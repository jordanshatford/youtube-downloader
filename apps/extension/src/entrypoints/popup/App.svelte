<script lang="ts">
	import { Card, Button } from '@yd/ui';
	import PopupWithContext from '@/lib/components/PopupWithContext.svelte';
</script>

<PopupWithContext let:ctx>
	{@const video = ctx.video}
	<Card>
		<img alt="Thumbnail" class="block h-auto w-full" src={video?.thumbnail} />
		<header class="flex items-center justify-between p-2 leading-tight md:p-4">
			<h1 class="line-clamp-2 text-lg text-zinc-900 dark:text-white">
				{video?.title}
			</h1>
			<p class="text-sm text-zinc-700 dark:text-zinc-300">{video?.duration}</p>
		</header>
		<footer class="flex items-center justify-between p-2 leading-none md:p-4">
			<div class="flex items-center text-zinc-800 dark:text-zinc-400">
				<img
					alt={video?.channel.name}
					class="block h-10 w-10 rounded-lg"
					src={video?.channel.thumbnail}
				/>
				<p class="ml-2 text-sm">
					{video?.channel.name}
				</p>
			</div>
		</footer>
	</Card>
	<Button disabled>Download</Button>
</PopupWithContext>
