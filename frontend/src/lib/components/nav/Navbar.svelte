<script lang="ts">
	import { page } from '$app/stores'
	import { goto } from '$app/navigation'
	import NotificationIconButton from '$lib/components/nav/NotificationIconButton.svelte'
	import ThemeChangeButton from '$lib/components/nav/ThemeChangeButton.svelte'
	import { routes, RoutePathConstants } from '$lib/utils/RouteUtils'
	import { download } from '$lib/components/icons'
	import { downloads } from '$lib/stores/downloads'
	import NavbarItem from '$lib/components/nav/NavbarItem.svelte'
	import Hamburger from '$lib/components/nav/mobile/Hamburger.svelte'
	import MobileMenu from '$lib/components/nav/mobile/MobileMenu.svelte'

	let menuOpen = false
</script>

<nav class="border-b dark:border-gray-700">
	<div class="max-w-7xl mx-auto px-2 sm:px-6 lg:px-8">
		<div class="relative flex items-center justify-between h-16">
			<Hamburger on:click={() => (menuOpen = !menuOpen)} isOpen={menuOpen} />
			<div class="flex-1 flex items-center justify-center sm:items-stretch sm:justify-start">
				<div class="flex-shrink-0 flex items-center">
					<img class="block h-8 w-auto" src="images/logo.png" alt="Logo" />
				</div>
				<div class="hidden sm:block sm:ml-6">
					<div class="flex space-x-4">
						{#each routes as route}
							<NavbarItem {route} />
						{/each}
					</div>
				</div>
			</div>
			<div
				class="absolute inset-y-0 right-0 flex items-center space-x-4 pr-2 sm:static sm:inset-auto sm:ml-6 sm:pr-0"
			>
				<NotificationIconButton
					on:click={() => goto(RoutePathConstants.DOWNLOADS)}
					active={$page.path === RoutePathConstants.DOWNLOADS}
					data={download}
					notifications={Object.keys($downloads).length}
				/>
				<ThemeChangeButton />
			</div>
		</div>
	</div>
	<MobileMenu isOpen={menuOpen} {routes} />
</nav>
