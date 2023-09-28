<script lang="ts">
	import { AudioFormat, DownloadQuality, DownloadType, VideoFormat } from '@yd/client';
	import { toast, Select, Title, Description } from '@yd/ui';
	import { settings } from '$lib/stores/settings';
	import { toSelectOptions, formatDescriptions } from '$lib/utils/settings';
	import config from '$lib/config';

	const lookup: Record<DownloadType, object> = {
		[DownloadType.AUDIO]: AudioFormat,
		[DownloadType.VIDEO]: VideoFormat
	};
</script>

<svelte:head>
	<title>Settings - {config.about.title}</title>
</svelte:head>

<div>
	<Title>Settings</Title>
	<Description>Set preferred settings for the videos you convert</Description>
	<div class="mx-auto max-w-xl overflow-hidden md:max-w-xl">
		<div class="mb-2 md:flex">
			<div class="mt-4 w-full">
				<Select
					on:change={() => toast.success('Updated', 'Quality settings updated successfully.')}
					title="Quality:"
					options={toSelectOptions(DownloadQuality)}
					bind:value={$settings.quality}
				/>
				<Select
					on:change={() => toast.success('Updated', 'Embedding settings updated successfully.')}
					title="Embed metadata:"
					options={toSelectOptions({ YES: true, NO: false })}
					bind:value={$settings.embed_metadata}
				/>
				<Select
					on:change={() => toast.success('Updated', 'Type settings updated successfully.')}
					title="Type:"
					options={toSelectOptions(DownloadType)}
					bind:value={$settings.type}
				/>
				<Select
					on:change={() => toast.success('Updated', 'Format settings updated successfully.')}
					title="Format:"
					options={toSelectOptions(lookup[$settings.type])}
					bind:value={$settings.format}
				/>
				<p class="mx-auto mt-4 max-w-xl text-center text-zinc-500">
					{formatDescriptions[$settings.format]}
				</p>
			</div>
		</div>
	</div>
</div>
