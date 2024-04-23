<script lang="ts">
	import '../app.css';

	import { page } from '$app/stores';
	import { setupSession } from '$lib/api';
	import Loading from '$lib/components/Loading.svelte';
	import Logo from '$lib/components/Logo.svelte';
	import config from '$lib/config';
	import { footerLinks, navbarLinks } from '$lib/routes';

	import { Footer, NavBar, ThemeToggle, Toasts } from '@yd/ui';
</script>

<svelte:head>
	<title>{config.head.title}</title>
	<meta name="keywords" content={config.head.keywords.join(', ')} />
	<meta name="description" content={config.head.description} />
	<meta property="og:url" content={config.head.url} />
	<meta property="og:title" content={config.head.title} />
	<meta property="og:description" content={config.head.description} />
	<meta property="og:image" content="/icons/icon-192x192.png" />
	<meta property="og:type" content="website" />
</svelte:head>

<Toasts position="bottom-right" />
<div class="h-full min-h-screen dark:bg-zinc-900">
	<div class="h-full">
		<NavBar links={navbarLinks} activeLink={$page.url.pathname}>
			<Logo slot="logo" />
			<ThemeToggle slot="right" />
		</NavBar>
		<main class="mx-auto h-full max-w-7xl px-4 pt-20 sm:px-6 lg:px-8">
			{#await setupSession()}
				<Loading />
			{:then}
				<slot />
			{/await}
		</main>
	</div>
</div>
<Footer copyright={config.copyright} links={footerLinks} githubLink={config.github} />
