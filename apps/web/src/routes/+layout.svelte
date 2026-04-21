<script lang="ts">
	import '../app.css';

	import type { Snippet } from 'svelte';
	import { setupSession } from '$lib/api';
	import AppThemeToggle from '$lib/components/app-theme-toggle.svelte';
	import AppBreadcrumbs from '$lib/components/breadcrumbs.svelte';
	import AppSidebar from '$lib/components/sidebar/sidebar.svelte';
	import config from '$lib/config';

	import { Empty, ModeWatcher, Separator, Sidebar, SpinnerIcon, Toaster } from '@yd/ui';

	interface Props {
		children?: Snippet;
	}

	let { children }: Props = $props();
</script>

<svelte:head>
	<title>{config.head.title}</title>
	<meta name="keywords" content={config.head.keywords.join(', ')} />
	<meta name="description" content={config.head.description} />
	<meta property="og:title" content={config.head.title} />
	<meta property="og:description" content={config.head.description} />
	<meta property="og:image" content="/icons/icon-192x192.png" />
	<meta property="og:type" content="website" />
</svelte:head>

<ModeWatcher />
<Toaster richColors closeButton position="bottom-right" />

<Sidebar.Provider open={false}>
	<AppSidebar collapsible="icon" />
	<Sidebar.Inset>
		<header
			class="bg-background sticky top-0 z-50 flex h-16 shrink-0 items-center gap-2 border-b px-0 transition-[width,height] ease-linear group-has-data-[collapsible=icon]/sidebar-wrapper:h-12"
		>
			<div class="flex items-center gap-2 px-4">
				<Sidebar.Trigger class="-ms-1" />
				<Separator.Root orientation="vertical" class="me-2 data-[orientation=vertical]:h-4" />
				<AppBreadcrumbs />
			</div>
			<div class="mr-5 ml-auto">
				<AppThemeToggle />
			</div>
		</header>
		<div class="flex flex-1 flex-col gap-4 p-4">
			<div class="flex justify-center">
				<div class="w-full px-4">
					{#await setupSession()}
						<Empty.Root>
							<Empty.Header>
								<Empty.Media variant="icon">
									<SpinnerIcon />
								</Empty.Media>
								<Empty.Title>Setting up session</Empty.Title>
								<Empty.Description>
									Setting up session, this may take some time on the first load as the backend
									starts up and initializes.
								</Empty.Description>
							</Empty.Header>
						</Empty.Root>
					{:then}
						{@render children?.()}
					{/await}
				</div>
			</div>
		</div>
	</Sidebar.Inset>
</Sidebar.Provider>
