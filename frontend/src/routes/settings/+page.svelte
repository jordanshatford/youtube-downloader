<script lang="ts">
	import { settings } from '$lib/stores/settings'
	import Select from '$lib/components/ui/Select.svelte'
	import { audioFormatOptions, audioFormatDescriptions } from '$lib/utils/audio-settings'
	import Title from '$lib/components/typography/Title.svelte'
	import Description from '$lib/components/typography/Description.svelte'
	import Alert from '$lib/components/ui/Alert.svelte'
	import { Variant } from '$lib/utils/types'
	import config from '$lib/config'

	let showSavedAlert = false

	function onSettingsChange() {
		showSavedAlert = true
		setTimeout(() => {
			showSavedAlert = false
		}, 3000)
	}
</script>

<svelte:head>
	<title>Settings - {config.app.title}</title>
</svelte:head>

<div>
	<Title>Settings</Title>
	<Description>Set preferred settings for the videos you convert</Description>
	<div class="max-w-xl mx-auto overflow-hidden md:max-w-xl">
		<div class="md:flex mb-2">
			<div class="w-full mt-4">
				<Select
					on:change={() => onSettingsChange()}
					title="Format:"
					options={audioFormatOptions}
					bind:value={$settings.format}
				/>
			</div>
		</div>
		{#if showSavedAlert}
			<Alert title="Setting Updated" variant={Variant.SUCCESS} />
		{/if}
	</div>
	<p class="text-center mt-4 max-w-xl mx-auto text-zinc-500">
		{audioFormatDescriptions[$settings.format]}
	</p>
</div>
