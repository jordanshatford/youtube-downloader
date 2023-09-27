<script lang="ts" context="module">
	import { OpenAPI } from '@yd/client';
	import { env } from '$lib/config';

	OpenAPI.BASE = env.serverAddress;
</script>

<script lang="ts">
	import '../app.css';
	import { onMount } from 'svelte';
	import { page } from '$app/stores';
	import { Toasts, NavBar, Footer, ThemeToggle } from '@yd/ui';
	import Loading from '$lib/components/Loading.svelte';
	import { session } from '$lib/stores/session';
	import { downloads } from '$lib/stores/downloads';
	import config from '$lib/config';
	import { navbarLinks, footerLinks } from '$lib/routes';
	import Logo from '$lib/components/Logo.svelte';

	// Use session as token when making requests with client
	OpenAPI.TOKEN = async () => {
		return $session;
	};

	$: if ($session) {
		downloads.setupStatusListener();
	}

	onMount(async () => {
		await session.setup();
	});
</script>

<Toasts position="bottom-right" />
<div class="h-full min-h-screen dark:bg-zinc-900">
	{#if $session}
		<div class="h-full">
			<NavBar links={navbarLinks} activeLink={$page.url.pathname}>
				<Logo slot="logo" />
				<ThemeToggle slot="right" />
			</NavBar>
			<main class="mx-auto h-full max-w-7xl px-4 pt-20 sm:px-6 lg:px-8">
				<slot />
			</main>
		</div>
	{:else}
		<Loading />
	{/if}
</div>
<Footer copyright={config.copyright} links={footerLinks} githubLink={config.github} />
