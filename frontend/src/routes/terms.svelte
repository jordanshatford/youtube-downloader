<script lang="ts">
	import Title from '$lib/components/typography/Title.svelte'
	import Description from '$lib/components/typography/Description.svelte'
	import List from '$lib/components/typography/List.svelte'
	import { termsOfUse, websiteName } from '$lib/utils/terms-of-use'
</script>

<svelte:head>
	<title>Terms of Use - Youtube to MP3</title>
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
