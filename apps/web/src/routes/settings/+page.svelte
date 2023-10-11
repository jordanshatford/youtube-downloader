<script lang="ts">
	import { AudioFormat, DownloadQuality, DownloadType, VideoFormat } from '@yd/client';
	import { Alert, toast, Select, Tabs, GearIcon, DownloadIcon, CodeBracketIcon } from '@yd/ui';
	import { settings, userSettings } from '$lib/stores/settings';
	import config from '$lib/config';

	function toSelectOptions<T extends object>(value: T) {
		return Object.entries(value).map(([key, value]) => {
			return {
				value,
				text: key
			};
		});
	}

	let tabs = [
		{
			key: 'downloadoptions',
			title: 'Download Options',
			icon: DownloadIcon
		},
		{
			key: 'embed',
			title: 'Embed Options',
			icon: CodeBracketIcon
		},
		{
			key: 'other',
			title: 'Other',
			icon: GearIcon
		}
	];

	let activePage = tabs[0].key;

	$: formatGroups = [
		{
			text: 'Audio',
			options: toSelectOptions(AudioFormat),
			disabled: $settings.type !== DownloadType.AUDIO
		},
		{
			text: 'Video',
			options: toSelectOptions(VideoFormat),
			disabled: $settings.type !== DownloadType.VIDEO
		}
	];

	function onTypeChange() {
		// Set default format based on type
		switch ($settings.type) {
			case DownloadType.VIDEO:
				$settings.format = VideoFormat.AVI;
				break;
			case DownloadType.AUDIO:
				$settings.format = AudioFormat.AAC;
				break;
		}
		toast.success('Updated', 'Type settings updated successfully.');
	}
</script>

<svelte:head>
	<title>Settings - {config.head.title}</title>
</svelte:head>

<div>
	<div class="mx-auto max-w-xl overflow-hidden md:max-w-xl">
		<Tabs {tabs} bind:active={activePage} />
		{#if activePage === 'downloadoptions'}
			<div class="mt-2">
				<Select
					id="type"
					label="Type:"
					bind:value={$settings.type}
					options={toSelectOptions(DownloadType)}
					on:change={onTypeChange}
				/>
				<Select
					id="format"
					label="Format:"
					bind:value={$settings.format}
					groups={formatGroups}
					on:change={() => toast.success('Updated', 'Format settings updated successfully.')}
				/>
				<Select
					id="quality"
					label="Quality:"
					bind:value={$settings.quality}
					options={toSelectOptions(DownloadQuality)}
					on:change={() => toast.success('Updated', 'Quality settings updated successfully.')}
				/>
			</div>
		{:else if activePage === 'embed'}
			<div class="mt-2">
				<Alert
					variant="warning"
					title="Warning!"
					description="Enabling these options could drastically increase the processing time."
				/>
				<Select
					id="metadata"
					label="Metadata:"
					helpText="Embed information from the video into the download."
					bind:value={$settings.embed_metadata}
					options={toSelectOptions({ YES: true, NO: false })}
					on:change={() =>
						toast.success('Updated', 'Metadata embedding settings updated successfully.')}
				/>
				<Select
					id="thumbnail"
					label="Thumbnail:"
					helpText="Attempt to embed thumbnail. May not always work."
					bind:value={$settings.embed_thumbnail}
					options={toSelectOptions({ YES: true, NO: false })}
					on:change={() =>
						toast.success('Updated', 'Thumbnail embedding settings updated successfully.')}
				/>
				<Select
					id="subtitles"
					label="Subtitles:"
					helpText="Attempt to embed subtitles. May not always work."
					bind:value={$settings.embed_subtitles}
					options={toSelectOptions({ YES: true, NO: false })}
					on:change={() =>
						toast.success('Updated', 'Subtitle embedding settings updated successfully.')}
				/>
			</div>
		{:else if activePage === 'other'}
			<div class="mt-2">
				<Select
					id="downloadPageSize"
					label="Downloads page size:"
					bind:value={$userSettings.downloadsPageSize}
					options={[...Array(11 + 5).keys()].slice(5).map((v) => ({ value: v, text: `${v}` }))}
					on:change={() =>
						toast.success('Updated', 'Downloads page size setting updated successfully.')}
				/>
				<Select
					id="autoDownload"
					label="Automatically download when complete:"
					bind:value={$userSettings.autoDownloadOnComplete}
					options={toSelectOptions({ YES: true, NO: false })}
					on:change={() =>
						toast.success('Updated', 'Automatic download settings updated successfully.')}
				/>
			</div>
		{/if}
	</div>
</div>
