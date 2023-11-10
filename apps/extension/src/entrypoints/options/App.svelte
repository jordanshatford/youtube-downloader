<script lang="ts">
	import { AudioFormat, DownloadQuality, VideoFormat } from '@yd/client';
	import {
		Alert,
		toast,
		Select,
		DownloadIcon,
		CodeBracketIcon,
		LoaderIcon,
		Icon,
		Toggle,
		toSelectOptions
	} from '@yd/ui';
	import { settings } from '~/lib/stores/settings';
	import PageLayout from '~/lib/components/PageLayout.svelte';

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

<PageLayout>
	{#await settings.initialize()}
		<div class="flex h-full w-full justify-center pt-20 text-zinc-800 dark:text-zinc-100">
			<Icon src={LoaderIcon} class="h-8 w-8 animate-spin" />
		</div>
	{:then}
		<div class="mx-auto max-w-xl overflow-hidden md:max-w-xl">
			<div class="flex items-center space-x-2 pb-2 text-2xl text-zinc-800 dark:text-zinc-100">
				<Icon src={DownloadIcon} class="h-8 w-8" />
				<p>Download Options</p>
			</div>
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
			<div class="flex items-center space-x-2 py-2 pt-8 text-2xl text-zinc-800 dark:text-zinc-100">
				<Icon src={CodeBracketIcon} class="h-8 w-8" />
				<p>Embedding Options</p>
			</div>
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
		</div>
	{/await}
</PageLayout>
