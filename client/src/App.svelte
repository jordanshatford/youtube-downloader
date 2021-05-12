<script lang="ts">
	import { onMount } from "svelte"
	import { Router } from "svelte-router-spa"
  	import { routes } from "./routes"
	import { theme } from "./stores/theme"
	import { session } from "./stores/session"
	import { Theme } from "./utils/types"

	onMount(async () => {
		if ($theme === Theme.DARK) {
			theme.applyDark()
        }
		await session.setup()
	});
</script>

<Router {routes} />

<style global>
	@tailwind base;
	@tailwind components;
	@tailwind utilities;
</style>