<script lang="ts">
	import { onMount } from "svelte"
	import { Router } from "svelte-router-spa"
  	import { routes } from "./routes"
	import { sessionStore } from "./stores/session"

	onMount(async () => {
		await sessionStore.setupSession()
	});
</script>

<Router {routes} />

<style global>
	@tailwind base;
	@tailwind components;
	@tailwind utilities;
</style>