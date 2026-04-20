<script lang="ts">
	import AppDownloadStatusIcon from '$lib/components/app-download-status-icon.svelte';
	import AppVideoInfo from '$lib/components/app-video-info.svelte';
	import config from '$lib/config';
	import { batch } from '$lib/stores/batch.svelte';
	import { debounce } from '$lib/utils/debounce';

	import {
		Alert,
		AlertCircleIcon,
		buttonVariants,
		ChevronsUpDownIcon,
		cn,
		Collapsible,
		CornerDownLeftIcon,
		FileDownloadIcon,
		InputGroup,
		MonitorPlayIcon,
		RotateIcon,
		Skeleton,
		SpinnerIcon,
		Tooltip,
		TrashIcon
	} from '@yd/ui';

	let text = $state(batch.text);

	let isBatchInputDisabled = $derived<boolean>(batch.isLoading || batch.batch !== undefined);
	let isBatchSubmitDisabled = $derived<boolean>(
		isBatchInputDisabled || (batch.batch === undefined && !batch.hasURLs)
	);

	const onInput = debounce(() => {
		batch.text = text;
	});
</script>

<svelte:head>
	<title>Batch Download - {config.head.title}</title>
</svelte:head>

<div class="mx-auto grid w-full max-w-2xl gap-8">
	<InputGroup.Root>
		<InputGroup.Addon align="block-start" class="border-b">
			<InputGroup.Text class="font-medium">
				<MonitorPlayIcon />
				YouTube Video URLs:
			</InputGroup.Text>
			{#if batch.isLoading}
				<InputGroup.Text class="ms-auto">
					{batch.nDone}/{batch.nTotal}
					<SpinnerIcon />
				</InputGroup.Text>
			{:else}
				<Tooltip.Provider>
					<Tooltip.Root>
						<Tooltip.Trigger
							class={cn('ms-auto', buttonVariants({ size: 'icon-sm', variant: 'ghost' }))}
							disabled={batch.isDownloadDisabled}
							onclick={async () => await batch.getFile()}><FileDownloadIcon /></Tooltip.Trigger
						>
						<Tooltip.Content>Download ZIP</Tooltip.Content>
					</Tooltip.Root>
					<Tooltip.Root>
						<Tooltip.Trigger
							class={buttonVariants({ size: 'icon-sm', variant: 'ghost' })}
							disabled={batch.isRetryDisabled}
							onclick={async () => await batch.restart()}
						>
							<RotateIcon />
						</Tooltip.Trigger>
						<Tooltip.Content>Retry</Tooltip.Content>
					</Tooltip.Root>
					<Tooltip.Root>
						<Tooltip.Trigger
							class={buttonVariants({ size: 'icon-sm', variant: 'ghost' })}
							disabled={batch.isDeleteDisabled}
							onclick={async () => {
								await batch.remove();
								text = batch.text;
							}}
						>
							<TrashIcon />
						</Tooltip.Trigger>
						<Tooltip.Content>Delete</Tooltip.Content>
					</Tooltip.Root>
				</Tooltip.Provider>
			{/if}
		</InputGroup.Addon>
		<InputGroup.Textarea
			class="max-h-100 min-h-50"
			disabled={isBatchInputDisabled}
			bind:value={text}
			oninput={onInput}
		/>
		<InputGroup.Addon align="block-end" class="border-t">
			<InputGroup.Text class="text-xs font-medium"
				>{batch.textUniqueUrls.length} unique URL(s) detected.</InputGroup.Text
			>
			<InputGroup.Button
				size="sm"
				class="ms-auto"
				variant="default"
				disabled={isBatchSubmitDisabled}
				onclick={async () => await batch.add()}
			>
				Submit<CornerDownLeftIcon />
			</InputGroup.Button>
		</InputGroup.Addon>
	</InputGroup.Root>
	{#if batch.isOverallError}
		<Alert.Root variant="destructive">
			<AlertCircleIcon />
			<Alert.Title>Error downloading batch of URLs.</Alert.Title>
		</Alert.Root>
	{/if}
	{#if batch.hasTooManyURLs}
		<Alert.Root variant="destructive">
			<AlertCircleIcon />
			<Alert.Title>A maximum of 25 URLs can be used with batch downloading.</Alert.Title>
		</Alert.Root>
	{/if}
	{#if batch.batch && !batch.isOverallError}
		<Collapsible.Root class="w-full space-y-2">
			<div class="flex items-center justify-between space-x-4 px-4">
				<h4 class="text-sm">
					Downloaded {batch.nDone} item(s):
				</h4>
				<Collapsible.Trigger
					class={buttonVariants({ variant: 'ghost', size: 'sm', class: 'w-9 p-0' })}
				>
					<ChevronsUpDownIcon />
					<span class="sr-only">Toggle</span>
				</Collapsible.Trigger>
			</div>
			{#if batch.current}
				<div
					class="flex items-center justify-between rounded-md border p-1 pr-2 text-sm font-medium"
				>
					<AppVideoInfo video={batch.current.video} />
					<AppDownloadStatusIcon status={batch.current?.status} />
				</div>
			{:else}
				<div
					class="flex items-center justify-between rounded-md border p-2 pr-2 text-sm font-medium"
				>
					<div class="flex items-center space-x-3">
						<Skeleton class="hidden aspect-video h-10 md:flex" />
						<Skeleton class="h-10 w-75" />
					</div>
					<Skeleton class="size-9" />
				</div>
			{/if}
			<Collapsible.Content class="space-y-2">
				{#each batch.others as item (item.video.id)}
					<div
						class="flex items-center justify-between rounded-md border p-1 pr-2 text-sm font-medium"
					>
						<AppVideoInfo video={item.video} />
						<AppDownloadStatusIcon status={item.status} />
					</div>
				{/each}
			</Collapsible.Content>
		</Collapsible.Root>
	{/if}
</div>
