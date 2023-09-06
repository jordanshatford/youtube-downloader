<script lang="ts" context="module">
	import { OpenAPI } from '@yd/client';
	import { env } from '$lib/config';

	OpenAPI.BASE = env.serverAddress;
</script>

<script lang="ts">
	import '../app.css';
	import { onMount } from 'svelte';
	import { Toasts, Footer } from '@yd/ui';
	import Nav from '$lib/components/nav/Nav.svelte';
	import Loading from '$lib/components/Loading.svelte';
	import { session } from '$lib/stores/session';
	import { downloads } from '$lib/stores/downloads';
	import config from '$lib/config';
	import { RoutePathConstants } from '$lib/utils/route';

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
<div class="min-h-screen h-full dark:bg-zinc-900">
	{#if $session}
		<div class="h-full">
			<Nav />
			<main class="h-full max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-20">
				<slot />
			</main>
		</div>
	{:else}
		<Loading />
	{/if}
</div>
<Footer
	copyright={config.copyright}
	links={[
		{
			href: RoutePathConstants.FAQ,
			title: 'faq'
		},
		{
			href: RoutePathConstants.TERMS_OF_USE,
			title: 'terms of use'
		}
	]}
	githubLink={config.github}
/>
