<script lang="ts">
	import { Title, Description, List } from '@yd/ui';
	import { termsOfUse, websiteName } from '$lib/utils/terms-of-use';
	import config from '$lib/config';
</script>

<svelte:head>
	<title>Terms of Use - {config.head.title}</title>
</svelte:head>

<div class="pb-6">
	<Title>Terms of Use</Title>
	<Description>
		By using {websiteName}, you agree to be bound by the following terms of use:
	</Description>
	<List items={termsOfUse} />
	<Description>
		{websiteName} serves you on a legal basis. Do not download any copyrighted materials without permission.
	</Description>
</div>
