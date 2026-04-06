<script lang="ts">
	import { resolve } from '$app/paths';
	import DownloadsTable from '$lib/components/downloads-table/table.svelte';
	import config from '$lib/config';
	import { downloads } from '$lib/stores/downloads.svelte';

	import { ArrowUpRightIcon, Button, DownloadIcon, Empty } from '@yd/ui';

	const data = $derived(Object.values(downloads.downloads));
</script>

<svelte:head>
	<title>Downloads - {config.head.title}</title>
</svelte:head>

{#if data.length > 0}
	<DownloadsTable {data} />
{:else}
	<Empty.Root>
		<Empty.Header>
			<Empty.Media variant="icon">
				<DownloadIcon />
			</Empty.Media>
			<Empty.Title>No downloads yet.</Empty.Title>
			<Empty.Description>
				You haven't added any downloads yet. Get started by adding some using the search page.
			</Empty.Description>
		</Empty.Header>
		<Empty.Content>
			<div class="flex gap-2">
				<Button.Root variant="link" class="text-muted-foreground" size="sm">
					<a href={resolve('/')}>
						Search <ArrowUpRightIcon class="inline" />
					</a>
				</Button.Root>
			</div>
		</Empty.Content>
	</Empty.Root>
{/if}
