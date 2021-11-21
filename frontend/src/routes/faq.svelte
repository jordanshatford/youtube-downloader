<script lang="ts">
	import Title from '$lib/components/typography/Title.svelte'
	import Description from '$lib/components/typography/Description.svelte'
	import List from '$lib/components/typography/List.svelte'
	import { faqs } from '$lib/utils/faq'
</script>

<svelte:head>
	<title>FAQ - Youtube to MP3</title>
</svelte:head>

<div>
	<Title>FAQ</Title>
	<Description>Frequently Asked Questions</Description>
	<List items={faqs} />
</div>
