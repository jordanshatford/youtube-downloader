<script lang="ts">
	import type { Snippet } from 'svelte';

	import { ExternalLinkIcon, Footer, IconButton, initializeTheme, Toasts } from '@yd/ui';

	import config from '~/lib/config';
	import { openWebsite } from '~/lib/website';

	interface Props {
		children?: Snippet;
	}

	let { children }: Props = $props();

	// Ensure theme is set based on user preferences.
	initializeTheme();
</script>

<Toasts position="bottom-right" />
<div class="h-full min-h-screen dark:bg-zinc-900">
	<main class="mx-auto h-full max-w-7xl px-4 sm:px-6 lg:px-8">
		<div class="mx-auto max-w-xl overflow-hidden md:max-w-xl">
			<div class="flex w-full items-center justify-between py-10">
				<img src="/icon-128.png" alt="Logo" class="h-12 w-12" />
				<div class="flex space-x-2 text-zinc-500 dark:text-zinc-400">
					<IconButton
						title="Go to site"
						src={ExternalLinkIcon}
						onclick={openWebsite}
						class="h-6 w-6"
					/>
				</div>
			</div>
			{@render children?.()}
		</div>
	</main>
</div>
<Footer copyright={config.copyright} githubLink={config.github} />
