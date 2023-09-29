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
			key: 'general',
			title: 'General',
			icon: GearIcon
		},
		{
			key: 'downloadoptions',
			title: 'Download Options',
			icon: DownloadIcon
		}
	];

	let activePage = tabs[0].key;

	const lookup: Record<DownloadType, object> = {
		[DownloadType.AUDIO]: AudioFormat,
		[DownloadType.VIDEO]: VideoFormat
	};
</script>

<svelte:head>
	<title>Settings - {config.head.title}</title>
</svelte:head>

<div>
	<div class="mx-auto max-w-xl overflow-hidden md:max-w-xl">
		<Tabs {tabs} bind:active={activePage} />
		{#if activePage === 'general'}
			<div class="mt-2">
				<Select
					id="autoDownload"
					on:change={() =>
						toast.success('Updated', 'Automatic download settings updated successfully.')}
					title="Automatically download when complete:"
					options={toSelectOptions({ YES: true, NO: false })}
					bind:value={$userSettings.autoDownloadOnComplete}
				/>
			</div>
		{:else if activePage === 'downloadoptions'}
			<div class="mt-2">
				<Select
					id="quality"
					on:change={() => toast.success('Updated', 'Quality settings updated successfully.')}
					title="Quality:"
					options={toSelectOptions(DownloadQuality)}
					bind:value={$settings.quality}
				/>
				<Select
					id="metadata"
					on:change={() => toast.success('Updated', 'Embedding settings updated successfully.')}
					title="Embed metadata:"
					options={toSelectOptions({ YES: true, NO: false })}
					bind:value={$settings.embed_metadata}
				/>
				<Select
					id="type"
					on:change={() => toast.success('Updated', 'Type settings updated successfully.')}
					title="Type:"
					options={toSelectOptions(DownloadType)}
					bind:value={$settings.type}
				/>
				<Select
					id="format"
					on:change={() => toast.success('Updated', 'Format settings updated successfully.')}
					title="Format:"
					options={toSelectOptions(lookup[$settings.type])}
					bind:value={$settings.format}
				/>
			</div>
		{/if}
	</div>
</div>
