<script lang="ts">
	import type { DownloadOptions } from '@yd/client';
	export let options: DownloadOptions;

	const embed: string[] = [];
	if (options.embed_metadata) {
		embed.push('Metadata');
	}
	if (options.embed_thumbnail) {
		embed.push('Thumbnail');
	}
	if (options.embed_subtitles) {
		embed.push('Subtitles');
	}
</script>

<div class="w-full px-6 py-2">
	<p>Format: {options.format.toUpperCase()}</p>
	<p>Quality: {options.quality.toUpperCase()}</p>
	<p>Embed: {embed.join(', ')}</p>
</div>
