<script lang="ts">
	import Heading from '$lib/components/typography/Heading.svelte'
	import Title from '$lib/components/typography/Title.svelte'
	import Description from '$lib/components/typography/Description.svelte'
	import { downloads } from '$lib/stores/downloads'
	import DownloadsTable from '$lib/components/downloads/DownloadsTable.svelte'
	import Alert from '$lib/components/Alert.svelte'
	import { Variant } from '$lib/utils/types'

	const warningMessage =
		'If a video is stuck waiting or downloading for a long time, you may need to cancel it and start it again or refresh the page.'
</script>

<svelte:head>
	<title>Downloads - Youtube to MP3</title>
</svelte:head>

<div>
	<Heading>Youtube to MP3</Heading>
	<Title>View Downloads</Title>
	<Description>Here are all the videos you have downloaded to MP3.</Description>
	<div class="mmb-4 mt-4">
		<Alert title={'Warning:'} message={warningMessage} variant={Variant.WARNING} />
	</div>
	<div class="flex flex-col mt-4">
		<div class="overflow-x-auto sm:-mx-6 lg:-mx-8">
			<div class="py-2 align-middle inline-block min-w-full sm:px-6 lg:px-8">
				<div
					class="shadow overflow-hidden border-b border-gray-200 dark:border-gray-800 sm:rounded-lg"
				>
					<DownloadsTable items={$downloads} />
				</div>
			</div>
		</div>
	</div>
</div>
