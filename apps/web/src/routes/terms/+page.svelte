<script lang="ts">
	import config from '$lib/config';
	import { termsOfUse, websiteName } from '$lib/utils/terms-of-use';

	import { Title } from '@yd/ui';
</script>

<svelte:head>
	<title>Terms of Use - {config.head.title}</title>
</svelte:head>

<div class="pb-6">
	<Title>Terms of Use</Title>
	<p class="mx-auto mt-4 max-w-2xl text-center text-lg text-zinc-700 dark:text-zinc-400">
		By using {websiteName}, you agree to be bound by the following terms of use:
	</p>
	<ol class="mx-6 list-decimal py-6 text-left md:mx-32">
		{#each termsOfUse as termOfUse}
			<li class="mt-3 text-zinc-700 dark:text-zinc-300">{termOfUse.title}</li>
			{#if termOfUse.description}
				<p class="mt-1 text-zinc-500">{termOfUse.description}</p>
			{/if}
		{/each}
	</ol>
	<p class="mx-auto mt-4 max-w-2xl text-center text-lg text-zinc-700 dark:text-zinc-400">
		{websiteName} serves you on a legal basis. Do not download any copyrighted materials without permission.
	</p>
</div>
