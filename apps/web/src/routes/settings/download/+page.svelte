<script lang="ts">
	import { settings } from '$lib/stores/settings.svelte';
	import {
		toSelectedTextFromGroup,
		toSelectedTextFromOptions,
		toSelectGroups,
		toSelectOptions
	} from '$lib/utils/select';

	import { AudioFormat, DownloadQuality, VideoFormat } from '@yd/client';
	import { Button, Field, Select, Tabs, toast } from '@yd/ui';

	let form = $state($state.snapshot(settings.settings));

	let isFormDirty = $derived(settings.isDifferentThan(form));

	const formatGroups = toSelectGroups({
		Audio: AudioFormat,
		Video: VideoFormat
	});
	const formatText = $derived(toSelectedTextFromGroup(formatGroups, form.format));

	const qualityOptions = toSelectOptions(DownloadQuality);
	const qualityText = $derived(toSelectedTextFromOptions(qualityOptions, form.quality));

	function onCancel() {
		form = $state.snapshot(settings.settings);
	}

	function onSave(event: Event) {
		event.preventDefault();
		settings.settings = form;
		toast.success('Download settings saved successfully.');
		form = $state.snapshot(settings.settings);
	}
</script>

<Tabs.Content value="/settings/download">
	<form onsubmit={onSave}>
		<Field.Group>
			<Field.Separator />
			<Field.Field>
				<Field.Label for="format">Format:</Field.Label>
				<Select.Root type="single" required bind:value={form.format}>
					<Select.Trigger id="format" class="w-full">{formatText}</Select.Trigger>
					<Select.Content>
						{#each formatGroups as group (group.label)}
							<Select.Group>
								<Select.Label>{group.label}</Select.Label>
								{#each group.options as option (option.value)}
									<Select.Item value={option.value} label={option.label}>
										{option.label}
									</Select.Item>
								{/each}
							</Select.Group>
						{/each}
					</Select.Content>
				</Select.Root>
				<Field.Description>The format of file you want for the download.</Field.Description>
			</Field.Field>
			<Field.Field>
				<Field.Label for="quality">Quality:</Field.Label>
				<Select.Root type="single" required bind:value={form.quality}>
					<Select.Trigger id="quality" class="w-full">{qualityText}</Select.Trigger>
					<Select.Content>
						{#each qualityOptions as option (option.value)}
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
