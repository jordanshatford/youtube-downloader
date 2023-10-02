<script lang="ts">
	import { AudioFormat, DownloadQuality, DownloadType, VideoFormat } from '@yd/client';
	import { toast, Select, Tabs, GearIcon, DownloadIcon } from '@yd/ui';
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
					title="Type:"
					bind:value={$settings.type}
					options={toSelectOptions(DownloadType)}
					on:change={onTypeChange}
				/>
				<Select
					id="format"
					title="Format:"
					bind:value={$settings.format}
					groups={formatGroups}
					on:change={() => toast.success('Updated', 'Format settings updated successfully.')}
				/>
				<Select
					id="quality"
					title="Quality:"
					bind:value={$settings.quality}
					options={toSelectOptions(DownloadQuality)}
					on:change={() => toast.success('Updated', 'Quality settings updated successfully.')}
				/>
				<Select
					id="metadata"
					title="Embed metadata:"
					bind:value={$settings.embed_metadata}
					options={toSelectOptions({ YES: true, NO: false })}
					on:change={() => toast.success('Updated', 'Embedding settings updated successfully.')}
				/>
			</div>
		{:else if activePage === 'other'}
			<div class="mt-2">
				<Select
					id="downloadPageSize"
					title="Downloads page size:"
					bind:value={$userSettings.downloadsPageSize}
					options={[...Array(11 + 5).keys()].slice(5).map((v) => ({ value: v, text: `${v}` }))}
					on:change={() =>
						toast.success('Updated', 'Downloads page size setting updated successfully.')}
				/>
				<Select
					id="autoDownload"
					title="Automatically download when complete:"
					bind:value={$userSettings.autoDownloadOnComplete}
					options={toSelectOptions({ YES: true, NO: false })}
					on:change={() =>
						toast.success('Updated', 'Automatic download settings updated successfully.')}
				/>
			</div>
		{/if}
	</div>
</div>
