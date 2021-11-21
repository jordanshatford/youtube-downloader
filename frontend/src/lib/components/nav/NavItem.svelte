<script lang="ts">
	import { page } from '$app/stores'
	import type { Route } from '$lib/utils/route'

	export let route: Route
	export let isMobileMenu = false

	$: classNames =
		$page.path === route.path
			? 'text-gray-700 dark:text-white bg-gray-100 dark:bg-gray-900'
			: 'text-gray-400 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700'
</script>

<a on:click href={route.path} class:block={isMobileMenu} class="{classNames} px-3 py-2 rounded-md">
	{route.label}
</a>
