<script lang="ts">
	import { AudioFormat, DownloadQuality, DownloadType, VideoFormat } from '@yd/client';
	import { toast, Select, Tabs, GearIcon } from '@yd/ui';
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

	let tabs = [
		{
			key: 'all',
			title: 'All Settings',
			icon: GearIcon
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
		{#if activePage === 'all'}
			<div class="mb-2 md:flex">
				<div class="mt-4 w-full">
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
			</div>
		{/if}
	</div>
</div>
