<script lang="ts">
	import { onMount } from "svelte"
	import { Router } from "svelte-router-spa"
  	import { routes } from "./routes"
	import { sessionStore } from "./stores/session"
	import { downloadsStore } from "./stores/downloads"

	onMount(async () => {
		await sessionStore.setupSession()
		downloadsStore.setupDownloadStatusListener()
	});
</script>

<Router {routes} />

<style global>
	@tailwind base;
	@tailwind components;
	@tailwind utilities;
</style>