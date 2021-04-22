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
    <DownloadsTable downloadsInfo={$downloadsStore} />
</div>