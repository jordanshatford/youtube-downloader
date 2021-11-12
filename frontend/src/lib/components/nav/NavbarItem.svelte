<script lang="ts">
	import { page } from '$app/stores'
	import type { Route } from '$lib/utils/RouteUtils'

	export let route: Route
	export let isSidebar = false

	$: classNames = `${
		$page.path === route.path
			? 'border-indigo-800 dark:border-indigo-600 bg-gray-100 dark:bg-gray-800'
			: ''
	}`
</script>

{#if isSidebar}
	<a class="cursor-pointer" href={route.path}>
		<li class="text-gray-800">
			<div
				class="{classNames} hover:text-indigo-800 dark:hover:text-indigo-600 text-gray-500 dark:text-gray-300 px-6 py-4 flex items-center border-l-2 border-transparent"
			>
				<div class="w-6 h-6 md:w-8 md:h-8">
					<svelte:component this={route.icon} size="1.5x" class="mr-2" />
				</div>
				<p class="xl:text-base ml-3">{route.label}</p>
			</div>
		</li>
	</a>
{:else}
	<a
		href={route.path}
		class="{classNames} px-4 h-full hover:text-indigo-800 dark:hover:text-indigo-600 text-gray-500 dark:text-gray-300 focus:outline-none border-b-2 border-transparent cursor-pointer h-full flex items-center text-sm text-gray-700 tracking-normal transition duration-150 ease-in-out"
	>
		<svelte:component this={route.icon} size="1.5x" class="mr-2" />
		{route.label}
	</a>
{/if}
