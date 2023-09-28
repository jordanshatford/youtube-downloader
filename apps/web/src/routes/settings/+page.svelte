<script lang="ts">
	import { AudioFormat, DownloadQuality, DownloadType, VideoFormat } from '@yd/client';
	import { toast, Select, Title, Description } from '@yd/ui';
	import { settings } from '$lib/stores/settings';
	import config from '$lib/config';

	function toSelectOptions<T extends object>(value: T) {
		return Object.entries(value).map(([key, value]) => {
			return {
				value,
				text: key
			};
		});
	}

	const lookup: Record<DownloadType, object> = {
		[DownloadType.AUDIO]: AudioFormat,
		[DownloadType.VIDEO]: VideoFormat
	};
</script>

<svelte:head>
	<title>Settings - {config.head.title}</title>
</svelte:head>

<div>
	<Title>Settings</Title>
	<Description>Set preferred settings for the videos you download and convert.</Description>
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
			</div>
		</div>
	</div>
</div>
