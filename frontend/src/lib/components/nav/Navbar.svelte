<script lang="ts">
	import Logo from '$lib/components/ui/Logo.svelte'
	import type { Route } from '$lib/utils/RouteUtils'
	import NavbarItem from '$lib/components/nav/NavbarItem.svelte'
	import ThemeChangeIcon from '$lib/components/ui/ThemeChangeIcon.svelte'
	import NotificationIcon from '$lib/components/ui/NotificationIcon.svelte'

	export let routes: Route[]
</script>

<nav
	class="w-full bg-white hidden md:block shadow dark:shadow-dark fixed top-0 z-40 dark:bg-gray-900"
>
	<div class="container px-6 h-16 flex justify-between items-center lg:items-stretch mx-auto">
		<div class="flex items-center h-full">
			<div class="flex items-center mr-10">
				<Logo />
			</div>
			<ul class="hidden md:flex items-center h-full">
				{#each routes as route}
					<NavbarItem {route} />
				{/each}
			</ul>
		</div>
		<div class="h-full hidden sm:flex items-center justify-end">
			<div class="h-full flex items-center">
				<ThemeChangeIcon />
				<NotificationIcon />
			</div>
		</div>
	</div>
</nav>
