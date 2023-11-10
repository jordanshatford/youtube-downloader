<script lang="ts">
	import { IconButton, ExternalLinkIcon, Toasts, Footer } from '@yd/ui';
	import { initializeTheme } from '~/lib/theme';
	import config from '~/lib/config';

	// Ensure theme is set based on user preferences.
	initializeTheme();

	// Navigate user to webpage of YouTube Downloader.
	async function openWebpage() {
		await browser.tabs.create({ url: config.website });
	}
</script>

<Toasts position="bottom-right" />
<div class="h-full min-h-screen dark:bg-zinc-900">
	<main class="mx-auto h-full max-w-7xl px-4 sm:px-6 lg:px-8">
		<div class="mx-auto max-w-xl overflow-hidden md:max-w-xl">
			<div class="flex w-full items-center justify-between py-10">
				<img src="/icon/512.png" alt="Logo" class="h-12 w-12" />
				<div class="flex space-x-2 text-zinc-500 dark:text-zinc-400">
					<IconButton
						title="Go to site"
						src={ExternalLinkIcon}
						on:click={openWebpage}
						class="h-6 w-6"
					/>
				</div>
			</div>
			<slot />
		</div>
	</main>
</div>
<Footer copyright={config.copyright} githubLink={config.github} />
