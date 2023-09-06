<script lang="ts">
	import { toast, Select } from '@yd/ui';
	import { settings } from '$lib/stores/settings';
	import { audioFormatOptions, audioFormatDescriptions } from '$lib/utils/audio-settings';
	import Title from '$lib/components/typography/Title.svelte';
	import Description from '$lib/components/typography/Description.svelte';
	import config from '$lib/config';
</script>

<svelte:head>
	<title>Settings - {config.about.title}</title>
</svelte:head>

<div>
	<Title>Settings</Title>
	<Description>Set preferred settings for the videos you convert</Description>
	<div class="max-w-xl mx-auto overflow-hidden md:max-w-xl">
		<div class="md:flex mb-2">
			<div class="w-full mt-4">
				<Select
					on:change={() => toast.success('Settings saved successfully.')}
					title="Format:"
					options={audioFormatOptions}
					bind:value={$settings.format}
				/>
			</div>
		</div>
	</div>
	<p class="text-center mt-4 max-w-xl mx-auto text-zinc-500">
		{audioFormatDescriptions[$settings.format]}
	</p>
</div>
