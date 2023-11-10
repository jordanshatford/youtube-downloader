<script lang="ts">
	import { IconButton, Icon, ExternalLinkIcon, GearIcon, LoaderIcon } from '@yd/ui';
	import { setupContext } from '~/lib/context';
	import { initializeTheme } from '~/lib/theme';
	import config from '~/lib/config';

	// Ensure theme is set based on user preferences.
	initializeTheme();

	// Navigate user to webpage of YouTube Downloader.
	async function openWebpage() {
		await browser.tabs.create({ url: config.website });
	}

	// Navigate user to options page.
	async function openOptionsPage() {
		await browser.runtime.openOptionsPage();
	}
</script>

<div class="max-h-[600px] min-h-[500px] w-[320px] bg-white dark:bg-zinc-900">
	<div class="align-start flex h-screen flex-col items-start justify-start space-y-4 pt-5">
		<!-- Header of the popup -->
		<div class="flex w-full items-center justify-between px-5">
			<img src="/icon/512.png" alt="Logo" class="h-7 w-7" />
			<div class="flex space-x-2 text-zinc-500 dark:text-zinc-400">
				<IconButton
					title="Go to site"
					src={ExternalLinkIcon}
					on:click={openWebpage}
					class="h-5 w-5"
				/>
				<IconButton title="Options" src={GearIcon} on:click={openOptionsPage} class="h-5 w-5" />
			</div>
		</div>
		<!-- Remaining content -->
		<div class="flex h-full w-full flex-col items-center space-y-2 text-zinc-900 dark:text-white">
			{#await setupContext()}
				<!-- Loader shown while awaiting context -->
				<div class="flex h-full flex-col items-center justify-center space-y-2">
					<Icon src={LoaderIcon} class="h-10 w-10 animate-spin" />
					<div>Getting context...</div>
				</div>
			{:then ctx}
				<!-- Slot show when context found -->
				<slot {ctx} />
			{:catch}
				<!-- Could not get context -->
				<div class="flex h-full flex-col items-center justify-center space-y-2 text-center">
					<h1 class="text-3xl font-black text-gray-300 dark:text-gray-600">Error</h1>
					<p class="mt-2 text-gray-500 dark:text-gray-400">
						Could not detect YouTube video in active tab.
					</p>
				</div>
			{/await}
		</div>
	</div>
</div>
