<script lang="ts">
	import config from '$lib/config';
	import { settings } from '$lib/stores/settings.svelte';
	import { toSelectOptions } from '$lib/utils/select';

	import { AudioFormat, DownloadQuality, VideoFormat } from '@yd/client';
	import { Field, Select, Tabs, toast } from '@yd/ui';

	const formatGroups = [
		{
			label: 'Audio',
			options: toSelectOptions(AudioFormat)
		},
		{
			label: 'Video',
			options: toSelectOptions(VideoFormat)
		}
	];

	const formatTriggerContent = $derived.by(() => {
		// REturn the lable of the current format or fallback
		return (
			formatGroups
				.find((g) => g.options.find((o) => o.value === settings.settings.format))
				?.options.find((o) => o.value === settings.settings.format)?.label || 'Select format'
		);
	});

	const qualityGroups = [
		{
			label: 'Quality',
			options: toSelectOptions(DownloadQuality)
		}
	];

	const qualityTriggerContent = $derived.by(() => {
		// REturn the lable of the current quality or fallback
		return (
			qualityGroups
				.find((g) => g.options.find((o) => o.value === settings.settings.quality))
				?.options.find((o) => o.value === settings.settings.quality)?.label || 'Select quality'
		);
	});
</script>

<svelte:head>
	<title>Settings - {config.head.title}</title>
</svelte:head>

<Tabs.Content value="/settings/download">
	<Field.Group>
		<Field.Separator />
		<Field.Field>
			<Field.Label for="format">Format:</Field.Label>
			<Select.Root
				type="single"
				bind:value={settings.settings.format}
				onValueChange={() => toast.success('Format settings updated successfully.')}
			>
				<Select.Trigger id="format" class="w-full">{formatTriggerContent}</Select.Trigger>
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
			<Select.Root
				type="single"
				bind:value={settings.settings.quality}
				onValueChange={() => toast.success('Quality settings updated successfully.')}
			>
				<Select.Trigger id="quality" class="w-full">{qualityTriggerContent}</Select.Trigger>
				<Select.Content>
					{#each qualityGroups as group (group.label)}
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
			<Field.Description>The preferred quality for the download.</Field.Description>
		</Field.Field>
		<Field.Separator />
	</Field.Group>
</Tabs.Content>
