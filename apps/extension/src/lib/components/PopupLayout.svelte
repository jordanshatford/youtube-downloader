<script lang="ts">
	import { IconButton, ExternalLinkIcon, GearIcon, initializeTheme } from '@yd/ui';
	import { openWebsite } from '~/lib/website';
	import { getContextService } from '~/lib/context-service';
	import PopupError from '~/lib/components/PopupError.svelte';
	import PopupLoader from '~/lib/components/PopupLoader.svelte';

	// Ensure theme is set based on user preferences.
	initializeTheme();

	// Get context service. This is to ensure current context is set.
	const context = getContextService();

	// Navigate user to options page.
	async function openOptionsPage() {
		await browser.runtime.openOptionsPage();
	}
</script>

<div class="max-h-[600px] min-h-[540px] w-[320px] overflow-scroll bg-white dark:bg-zinc-900">
	<div class="align-start flex h-screen flex-col items-start justify-start space-y-2 pt-5">
		<!-- Header of the popup -->
		<div class="flex w-full items-center justify-between px-5">
			<img src="/icon/512.png" alt="Logo" class="h-7 w-7" />
			<div class="flex space-x-2 text-zinc-500 dark:text-zinc-400">
				<IconButton
					title="Go to site"
					src={ExternalLinkIcon}
					on:click={openWebsite}
					class="h-5 w-5"
				/>
				<IconButton title="Options" src={GearIcon} on:click={openOptionsPage} class="h-5 w-5" />
			</div>
		</div>
		<!-- Remaining content -->
		<div
			class="flex h-full w-full flex-col items-center space-y-2 p-2 text-zinc-900 dark:text-white"
		>
			{#await context.get()}
				<PopupLoader />
			{:then ctx}
				<slot {ctx} />
			{:catch error}
				<PopupError message={error.message} />
			{/await}
		</div>
	</div>
</div>
