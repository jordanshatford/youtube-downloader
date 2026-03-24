<script lang="ts">
	import config from '$lib/config';
	import { settings } from '$lib/stores/settings.svelte';

	import { AudioFormat, DownloadQuality, LanguageCode, VideoFormat } from '@yd/client';
	import {
		Alert,
		CodeBracketIcon,
		DownloadIcon,
		Select,
		Tabs,
		toasts,
		Toggle,
		toSelectOptions
	} from '@yd/ui';

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
		}
	];

	let activePage = $state(tabs[0].key);

	const formatGroups = [
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
					bind:value={settings.settings.format}
					groups={formatGroups}
					onchange={() => toasts.success('Updated', 'Format settings updated successfully.')}
				/>
				<Select
					id="quality"
					label="Quality:"
					helpText="The preferred quality for the download."
					bind:value={settings.settings.quality}
					options={toSelectOptions(DownloadQuality)}
					onchange={() => toasts.success('Updated', 'Quality settings updated successfully.')}
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
					bind:checked={settings.settings.embed_metadata}
					onchange={() =>
						toasts.success('Updated', 'Metadata embedding settings updated successfully.')}
				/>
				<Toggle
					id="thumbnail"
					label="Thumbnail:"
					helpText="Attempt to embed thumbnail. Depending on other settings, this may not always work."
					bind:checked={settings.settings.embed_thumbnail}
					onchange={() =>
						toasts.success('Updated', 'Thumbnail embedding settings updated successfully.')}
				/>
				<Toggle
					id="subtitles"
					label="Subtitles:"
					helpText="Attempt to embed subtitles. Depending on other settings, this may not always work."
					bind:checked={settings.settings.embed_subtitles}
					onchange={() =>
						toasts.success('Updated', 'Subtitle embedding settings updated successfully.')}
				/>
				{#if settings.settings.embed_subtitles}
					<Select
						id="subtitleslanguage"
						label="Preferred Subtitles Language:"
						helpText="The preferred subtitle language for the download."
						bind:value={settings.settings.preferred_subtitles_language}
						options={toSelectOptions(LanguageCode)}
						onchange={() =>
							toasts.success(
								'Updated',
								'Preferred subtitles language setting updated successfully.'
							)}
					/>
				{/if}
			</div>
		{/if}
	</div>
</div>
