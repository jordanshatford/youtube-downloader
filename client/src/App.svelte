<script lang="ts">
	import { onMount } from "svelte"
	import { Router } from "svelte-router-spa"
  	import { routes } from "./routes"
	import { theme } from "./stores/theme"
	import { session } from "./stores/session"

	onMount(async () => {
		if ($theme === "dark") {
            document.querySelector("html").classList.add("dark")
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