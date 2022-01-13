<script lang="ts">
	import { page } from '$app/stores'
	import type { Route } from '$lib/utils/route'

	export let route: Route
	export let isMobileMenu = false

	$: classNames =
		$page.path === route.path
			? 'text-zinc-700 dark:text-white bg-zinc-100 dark:bg-zinc-900'
			: 'text-zinc-400 dark:text-zinc-300 hover:bg-zinc-100 dark:hover:bg-zinc-700'
</script>

<a on:click href={route.path} class:block={isMobileMenu} class="{classNames} px-3 py-2 rounded-lg">
	{route.label}
</a>
