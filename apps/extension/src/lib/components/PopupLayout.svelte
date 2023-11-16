<script lang="ts">
	import { IconButton, ExternalLinkIcon, GearIcon } from '@yd/ui';
	import { initializeTheme } from '~/lib/theme';
	import { openWebsite } from '~/lib/website';

	// Ensure theme is set based on user preferences.
	initializeTheme();

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
					on:click={openWebsite}
					class="h-5 w-5"
				/>
				<IconButton title="Options" src={GearIcon} on:click={openOptionsPage} class="h-5 w-5" />
			</div>
		</div>
		<!-- Remaining content -->
		<div class="flex h-full w-full flex-col items-center space-y-2 text-zinc-900 dark:text-white">
			<slot />
		</div>
	</div>
</div>
