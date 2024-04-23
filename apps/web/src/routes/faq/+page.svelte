<script lang="ts">
	import config from '$lib/config';
	import { faqs } from '$lib/utils/faq';

	import { CollapsibleSection, Title } from '@yd/ui';
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
