<script lang="ts">
	import { AudioFormat, DownloadQuality } from '@yd/client';
	import { toast, Select, Title, Description } from '@yd/ui';
	import { settings } from '$lib/stores/settings';
	import { toSelectOptions, audioFormatDescriptions } from '$lib/utils/audio-settings';
	import config from '$lib/config';
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
					on:change={() => toast.success('Settings saved successfully.')}
					title="Quality:"
					options={toSelectOptions(DownloadQuality)}
					bind:value={$settings.quality}
				/>
				<Select
					on:change={() => toast.success('Settings saved successfully.')}
					title="Embed metadata:"
					options={toSelectOptions({ YES: true, NO: false })}
					bind:value={$settings.embed_metadata}
				/>
				<Select
					on:change={() => toast.success('Settings saved successfully.')}
					title="Format:"
					options={toSelectOptions(AudioFormat)}
					bind:value={$settings.format}
				/>
				<p class="mx-auto mt-4 max-w-xl text-center text-zinc-500">
					{audioFormatDescriptions[$settings.format]}
				</p>
			</div>
		</div>
	</div>
</div>
