<script lang="ts">
	import { AudioFormat, DownloadQuality, VideoFormat } from '@yd/client';
	import {
		Alert,
		toast,
		Select,
		Tabs,
		GearIcon,
		DownloadIcon,
		CodeBracketIcon,
		Toggle
	} from '@yd/ui';
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
			options: toSelectOptions(AudioFormat)
		},
		{
			text: 'Video',
			options: toSelectOptions(VideoFormat)
		}
	];
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
					id="format"
					label="Format:"
					helpText="The format of file you want for the download."
					bind:value={$settings.format}
					groups={formatGroups}
					on:change={() => toast.success('Updated', 'Format settings updated successfully.')}
				/>
				<Select
					id="quality"
					label="Quality:"
					helpText="The preferred quality for the download."
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
				<Toggle
					id="metadata"
					label="Metadata:"
					helpText="Embed extracted information from the video into the download."
					bind:checked={$settings.embed_metadata}
					on:change={() =>
						toast.success('Updated', 'Metadata embedding settings updated successfully.')}
				/>
				<Toggle
					id="thumbnail"
					label="Thumbnail:"
					helpText="Attempt to embed thumbnail. Depending on other settings, this may not always work."
					bind:checked={$settings.embed_thumbnail}
					on:change={() =>
						toast.success('Updated', 'Thumbnail embedding settings updated successfully.')}
				/>
				<Toggle
					id="subtitles"
					label="Subtitles:"
					helpText="Attempt to embed subtitles. Depending on other settings, this may not always work."
					bind:checked={$settings.embed_subtitles}
					on:change={() =>
						toast.success('Updated', 'Subtitle embedding settings updated successfully.')}
				/>
			</div>
		{:else if activePage === 'other'}
			<div class="mt-2">
				<Select
					id="downloadPageSize"
					label="Downloads page size:"
					helpText="Size of each page on the downloads tab."
					bind:value={$userSettings.downloadsPageSize}
					options={[...Array(11 + 5).keys()].slice(5).map((v) => ({ value: v, text: `${v}` }))}
					on:change={() =>
						toast.success('Updated', 'Downloads page size setting updated successfully.')}
				/>
				<Toggle
					id="autoDownload"
					label="Automatically download when complete:"
					helpText="Once a download is complete it will automatically be downloaded to your device."
					bind:checked={$userSettings.autoDownloadOnComplete}
					on:change={() =>
						toast.success('Updated', 'Automatic download settings updated successfully.')}
				/>
			</div>
		{/if}
	</div>
</div>
