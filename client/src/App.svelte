<script lang="ts">
	import { onMount } from "svelte"
	import { Router } from "svelte-router-spa"
  	import { routes } from "./routes"
	import { theme } from "./stores/theme"
	import { sessionStore } from "./stores/session"
	import { downloadsStore } from "./stores/downloads"
	import { wifi } from "./lib/icons"
	import Icon from "./lib/Icon.svelte"
	import Error from "./lib/Error.svelte"

	onMount(async () => {
		if ($theme === "dark") {
            document.querySelector("html").classList.add("dark")
        }
		await sessionStore.setupSession()
		downloadsStore.setupDownloadStatusListener()
	});
</script>

{#if $sessionStore}
<Router {routes} />
{:else}
<Error
	code="503"
	description="Could not connect to internal server."
>
	<button
		slot="actions"
		type="button"
		on:click={_ => sessionStore.setupSession()}
		class="mt-8 rounded-md border-2 dark:text-white dark:hover:bg-gray-700 dark:bg-gray-900 border-gray-300 dark:border-gray-700 shadow-sm px-4 py-2 bg-white text-base font-medium text-gray-700 hover:bg-gray-50 focus:outline-none"
	>
		Retry Connection <Icon data={wifi} size={1.5} />
	</button>
</Error>
{/if}

<style global>
	@tailwind base;
	@tailwind components;
	@tailwind utilities;
</style>