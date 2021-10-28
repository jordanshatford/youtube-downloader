<script lang="ts">
	import MobileNav from '$lib/components/nav/MobileNav.svelte'
	import Navbar from '$lib/components/nav/Navbar.svelte'
	import { routes } from '$lib/utils/RouteUtils'
</script>

<div>
	<Navbar {routes} />
	<MobileNav {routes} />
</div>
