<script lang="ts">
	import Title from '$lib/components/typography/Title.svelte';
	import Description from '$lib/components/typography/Description.svelte';
	import { downloads } from '$lib/stores/downloads';
	import DownloadsTable from '$lib/components/downloads/DownloadsTable.svelte';
	import config from '$lib/config';
</script>

<svelte:head>
	<title>Downloads - {config.about.title}</title>
</svelte:head>

<div>
	<Title>Downloads</Title>
	<Description>View videos being converted to MP3</Description>
	<div class="flex flex-col mt-4">
		<div class="overflow-x-auto sm:-mx-6 lg:-mx-8">
			<div class="py-2 align-middle inline-block min-w-full sm:px-6 lg:px-8">
				<div
					class="rounded-lg shadow dark:shadow-dark overflow-hidden border border-zinc-200 dark:border-zinc-800"
				>
					<DownloadsTable items={$downloads} />
				</div>
			</div>
		</div>
	</div>
</div>
