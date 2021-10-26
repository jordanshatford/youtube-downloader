<script lang="ts">
	import '../app.css'
	import { onMount } from 'svelte'
	import Navbar from '$lib/components/nav/Navbar.svelte'
	import Notifications from '$lib/components/Notifications.svelte'
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

<div>
	{#if $session}
		<div class="dark:bg-gray-900">
			<Navbar />
			<main class="min-h-screen dark:bg-gray-900 max-w-7xl mt-8 mx-auto px-4 sm:px-6 lg:px-8">
				<slot />
			</main>
		</div>
	{:else}
		<Loading />
	{/if}
	<Notifications />
</div>
