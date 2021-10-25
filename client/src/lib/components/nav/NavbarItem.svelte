<script lang="ts">
	import { page } from '$app/stores'
	import Icon from '$lib/components/Icon.svelte'
	import type { Route } from '$lib/utils/types'

	export let route: Route
	export let dropdown = false

	$: isActive = $page.path === route.path
</script>

<a
	href={route.path}
	title={route.label}
	class="{isActive
		? 'bg-gray-50 dark:bg-gray-800'
		: 'dark:bg-gray-900'} hover:bg-gray-50 dark:hover:bg-gray-700 text-gray-500 dark:text-gray-200 hover:text-gray-700 {dropdown
		? 'block'
		: ''} px-3 py-2 rounded-md text-sm font-medium"
>
	<Icon data={route.icon} className="mb-1 mr-1" size={1.4} />
	{route.label}
</a>
