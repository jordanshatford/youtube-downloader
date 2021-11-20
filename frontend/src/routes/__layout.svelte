<script lang="ts">
	import '../app.css'
	import { onMount } from 'svelte'
	import Nav from '$lib/components/nav/Nav.svelte'
	import Footer from '$lib/components/Footer.svelte'
	import Notifications from '$lib/components/Notifications.svelte'
	import { notifications } from '$lib/stores/notifications'
	import Loading from '$lib/components/Loading.svelte'
	import { session } from '$lib/stores/session'
	import { downloads } from '$lib/stores/downloads'
	import { theme } from '$lib/stores/theme'
	import { Theme } from '$lib/utils/types'

	$: if ($session) {
		downloads.setupStatusListener()
	}

	onMount(async () => {
		if ($theme === Theme.DARK) {
			theme.applyDark()
		}
		await session.setup()
	})
</script>

<div class="min-h-screen h-full dark:bg-gray-900">
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
	<Notifications visible={$notifications.visible} />
</div>
<Footer />
