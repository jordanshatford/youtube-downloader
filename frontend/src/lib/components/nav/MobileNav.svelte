<script lang="ts">
	import { MenuIcon, XIcon } from 'svelte-feather-icons'
	import IconButton from '$lib/components/ui/IconButton.svelte'
	import Logo from '$lib/components/ui/Logo.svelte'
	import type { Route } from '$lib/utils/RouteUtils'
	import NavbarItem from '$lib/components/nav/NavbarItem.svelte'
	import ThemeChangeIcon from '$lib/components/ui/ThemeChangeIcon.svelte'
	import NotificationIcon from '$lib/components/ui/NotificationIcon.svelte'

	let show = false

	export let routes: Route[]
</script>

<nav>
	<div
		class="dark:bg-gray-900 dark:shadow-dark h-16 shadow py-4 px-6 w-full flex md:hidden justify-between items-center bg-white fixed top-0 z-40"
	>
		<div class="w-24 mr-10">
			<Logo />
		</div>
		<div>
			{#if !show}
				<IconButton
					on:click={() => (show = !show)}
					class="dark:text-gray-200 hover:text-indigo-800 dark:hover:text-indigo-600"
					icon={MenuIcon}
					size="1.5x"
				/>
			{/if}
		</div>
	</div>
	<div
		class={show
			? 'absolute xl:hidden w-full h-auto z-40'
			: 'absolute xl:hidden w-full h-full transform -translate-x-full z-40'}
		id="mobile-nav"
	>
		<div
			class="bg-gray-800 cursor-pointer bg-opacity-75 w-full h-full fixed top-0"
			on:click={() => (show = !show)}
		/>
		<div
			class="w-64 z-40 fixed overflow-y-auto top-0 right-0 bg-white shadow flex flex-col justify-between xl:hidden transition duration-150 ease-in-out"
		>
			<div class="dark:bg-gray-900 flex flex-col justify-between h-screen w-full">
				<div>
					<div class="px-6 pt-3 flex w-full items-center justify-between">
						<div class="flex flex-row flex-row-reverse w-full">
							<IconButton
								class="flex items-end dark:text-gray-200 hover:text-red-800 dark:hover:text-red-600"
								on:click={() => (show = !show)}
								icon={XIcon}
								size="1.5x"
							/>
						</div>
					</div>
					<ul class="mt-4">
						{#each routes as route}
							<div on:click={() => (show = false)}>
								<NavbarItem {route} isSidebar={true} />
							</div>
						{/each}
					</ul>
				</div>
				<div class="w-full mb-6 px-6">
					<div class="w-full border-t border-gray-300 dark:border-gray-600">
						<div class="w-auto flex items-center justify-between pt-4">
							<ul class="flex items-center justify-between justify-items-center w-full px-8">
								<ThemeChangeIcon />
								<NotificationIcon />
							</ul>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</nav>
