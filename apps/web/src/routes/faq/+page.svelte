<script lang="ts">
	import { Title, Description, List } from '@yd/ui';
	import { faqs } from '$lib/utils/faq';
	import config from '$lib/config';
</script>

<svelte:head>
	<title>FAQ - {config.about.title}</title>
</svelte:head>

<div>
	<Title>FAQ</Title>
	<Description>Frequently Asked Questions</Description>
	<List items={faqs} />
</div>
