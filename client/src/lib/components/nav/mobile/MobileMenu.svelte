<script lang="ts">
	import NavbarItem from '$lib/components/nav/NavbarItem.svelte'
	import type { Route } from '$lib/utils/RouteUtils'

	export let routes: Route[]
	export let isOpen: boolean
</script>

<div class="sm:hidden">
	{#if isOpen}
		<div class="px-2 pt-2 pb-3 space-y-1">
			{#each routes as route}
				<NavbarItem {route} dropdown={true} />
			{/each}
		</div>
	{/if}
</div>
