<script lang="ts">
	import { Title, CollapsibleSection } from '@yd/ui';
	import { faqs } from '$lib/utils/faq';
	import config from '$lib/config';
</script>

<svelte:head>
	<title>FAQ - {config.head.title}</title>
</svelte:head>

<div>
	<Title>Frequently Asked Questions</Title>
	<div class="space-y-4 py-8">
		{#each faqs as faq (faq.title)}
			<CollapsibleSection {...faq} />
		{/each}
	</div>
</div>
