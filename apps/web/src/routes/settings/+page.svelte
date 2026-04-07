<script lang="ts">
	import config from '$lib/config';
	import { settings } from '$lib/stores/settings.svelte';
	import { toSelectOptions } from '$lib/utils/select';

	import { AudioFormat, DownloadQuality, LanguageCode, VideoFormat } from '@yd/client';
	import {
		Alert,
		AlertCircleIcon,
		Checkbox,
		CodeIcon,
		DownloadIcon,
		Field,
		Select,
		Tabs,
		toast
	} from '@yd/ui';

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

	const subtitlesLanguageGroups = [
		{
			label: 'Language',
			options: toSelectOptions(LanguageCode)
		}
	];

	const subtitlesLanguageTriggerContent = $derived.by(() => {
		// REturn the lable of the current preferred subtitles language or fallback
		return (
			subtitlesLanguageGroups
				.find((g) =>
					g.options.find((o) => o.value === settings.settings.preferred_subtitles_language)
				)
				?.options.find((o) => o.value === settings.settings.preferred_subtitles_language)?.label ||
			'Select preferred subtitles language'
		);
	});
</script>

<svelte:head>
	<title>Settings - {config.head.title}</title>
</svelte:head>

<Tabs.Root value="download" class="mx-auto max-w-2xl">
	<Tabs.List>
		<Tabs.Trigger value="download"><DownloadIcon />Download Options</Tabs.Trigger>
		<Tabs.Trigger value="embed"><CodeIcon />Embed Options</Tabs.Trigger>
	</Tabs.List>
	<Tabs.Content value="download">
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
	<Tabs.Content value="embed">
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
				<Checkbox.Root
					id="metadata"
					bind:checked={settings.settings.embed_metadata}
					onCheckedChange={() => toast.success('Metadata embedding settings updated successfully.')}
				/>
				<Field.Content>
					<Field.Label for="metadata">Embed Metadata:</Field.Label>
					<Field.Description>
						Embed extracted information from the download into the resulting file.
					</Field.Description>
				</Field.Content>
			</Field.Field>
			<Field.Field orientation="horizontal">
				<Checkbox.Root
					id="thumbnail"
					bind:checked={settings.settings.embed_thumbnail}
					onCheckedChange={() =>
						toast.success('Thumbnail embedding settings updated successfully.')}
				/>
				<Field.Content>
					<Field.Label for="thumbnail">Embed Thumbnail:</Field.Label>
					<Field.Description>
						Attempt to embed the thumbnail in the resulting file. Depending on other settings, this
						may not always work.
					</Field.Description>
				</Field.Content>
			</Field.Field>
			<Field.Field orientation="horizontal">
				<Checkbox.Root
					id="subtitles"
					bind:checked={settings.settings.embed_subtitles}
					onCheckedChange={() => toast.success('Subtitle embedding settings updated successfully.')}
				/>
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
					bind:value={settings.settings.preferred_subtitles_language}
					disabled={!settings.settings.embed_subtitles}
					onValueChange={() =>
						toast.success('Preferred subtitles language setting updated successfully.')}
				>
					<Select.Trigger id="subtitleslanguage" class="w-full"
						>{subtitlesLanguageTriggerContent}</Select.Trigger
					>
					<Select.Content>
						{#each subtitlesLanguageGroups as group (group.label)}
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
</Tabs.Root>
