<svelte:head>
	<title>Downloads - Youtube to MP3</title>
</svelte:head>

<script lang="ts">
    import Heading from "../components/typography/Heading.svelte"
    import Title from "../components/typography/Title.svelte"
    import Description from "../components/typography/Description.svelte"
    import { downloadsStore } from "../stores/downloads.js"
    import DownloadsTable from "../components/downloads/DownloadsTable.svelte"
</script>

<div>
    <Heading>Youtube to MP3</Heading>
    <Title>View Downloads</Title>
    <Description>Here are all the videos you have downloaded to MP3.</Description>
    <div class="flex flex-col mt-4">
        <div class="overflow-x-auto sm:-mx-6 lg:-mx-8">
            <div class="py-2 align-middle inline-block min-w-full sm:px-6 lg:px-8">
                <div class="shadow overflow-hidden border-b border-gray-200 dark:border-gray-800 sm:rounded-lg">
                    <DownloadsTable downloads={$downloadsStore} />
                </div>
            </div>
        </div>
    </div>
</div>