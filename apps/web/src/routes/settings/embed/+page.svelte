<script lang="ts">
	import { settings } from '$lib/stores/settings.svelte';
	import { toSelectedTextFromOptions, toSelectOptions } from '$lib/utils/select';

	import { LanguageCode } from '@yd/client';
	import { Alert, AlertCircleIcon, Button, Checkbox, Field, Select, Tabs, toast } from '@yd/ui';

	let form = $state($state.snapshot(settings.settings));

	let isFormDirty = $derived(settings.isDifferentThan(form));

	const subtitlesOptions = toSelectOptions(LanguageCode);
	const subtitlesText = $derived(
		toSelectedTextFromOptions(subtitlesOptions, form.preferred_subtitles_language)
	);

	function onCancel() {
		form = $state.snapshot(settings.settings);
	}

	function onSave(event: Event) {
		event.preventDefault();
		settings.settings = form;
		toast.success('Embed settings saved successfully.');
		form = $state.snapshot(settings.settings);
	}
</script>

<Tabs.Content value="/settings/embed">
	<form onsubmit={onSave}>
		<Field.Group>
			<Field.Separator />
			<Alert.Root variant="destructive">
				<AlertCircleIcon />
				<Alert.Title
					>Enabling embedding related options can drastically increase the time it takes to process
					the download. Only enable these options if they are required.</Alert.Title
				>
			</Alert.Root>
			<Field.Field orientation="horizontal">
				<Checkbox.Root id="metadata" bind:checked={form.embed_metadata} />
				<Field.Content>
					<Field.Label for="metadata">Embed Metadata:</Field.Label>
					<Field.Description>
						Embed extracted information from the download into the resulting file.
					</Field.Description>
				</Field.Content>
			</Field.Field>
			<Field.Field orientation="horizontal">
				<Checkbox.Root id="thumbnail" bind:checked={form.embed_thumbnail} />
				<Field.Content>
					<Field.Label for="thumbnail">Embed Thumbnail:</Field.Label>
					<Field.Description>
						Attempt to embed the thumbnail in the resulting file. Depending on other settings, this
						may not always work.
					</Field.Description>
				</Field.Content>
			</Field.Field>
			<Field.Field orientation="horizontal">
				<Checkbox.Root id="subtitles" bind:checked={form.embed_subtitles} />
				<Field.Content>
					<Field.Label for="subtitles">Embed Subtitles:</Field.Label>
					<Field.Description>
						Attempt to embed the subtitles in the resulting file. Depending on other settings, this
						may not always work.
					</Field.Description>
				</Field.Content>
			</Field.Field>
			<Field.Field>
				<Field.Label for="subtitleslanguage">Preferred Subtitles Language:</Field.Label>
				<Select.Root
					type="single"
					required
					bind:value={form.preferred_subtitles_language}
					disabled={!form.embed_subtitles}
				>
					<Select.Trigger id="subtitleslanguage" class="w-full">{subtitlesText}</Select.Trigger>
					<Select.Content>
						{#each subtitlesOptions as option (option.value)}
							<Select.Item value={option.value} label={option.label}>
								{option.label}
							</Select.Item>
						{/each}
					</Select.Content>
				</Select.Root>
				<Field.Description>The preferred quality for the download.</Field.Description>
			</Field.Field>
			<Field.Separator />
			<Field.Field orientation="horizontal">
				<Button.Root type="submit" disabled={!isFormDirty}>Save</Button.Root>
				<Button.Root variant="outline" type="button" disabled={!isFormDirty} onclick={onCancel}
					>Cancel</Button.Root
				>
			</Field.Field>
		</Field.Group>
	</form>
</Tabs.Content>
