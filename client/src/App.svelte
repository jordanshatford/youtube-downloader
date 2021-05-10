<script lang="ts">
	import { onMount } from "svelte"
	import { Router } from "svelte-router-spa"
  	import { routes } from "./routes"
	import { theme } from "./stores/theme"
	import { sessionStore, sessionEndpoint } from "./stores/session"
	import { downloadsStore } from "./stores/downloads"
	import { refresh } from "./lib/icons"
	import Icon from "./lib/Icon.svelte"
	import Error from "./lib/Error.svelte"
	import Loading from "./lib/Loading.svelte"

	async function setupSession() {
        let response = await fetch(sessionEndpoint).catch(e => {
			return Promise.reject("Could not setup session with internal server.")
		})
		
		let responseJson = await response.json()
		$sessionStore = responseJson.sessionId
		if ($sessionStore) {
			downloadsStore.setupDownloadStatusListener()
		}
	}

	let session = setupSession()

	onMount(() => {
		if ($theme === "dark") {
            document.querySelector("html").classList.add("dark")
        }
	});
</script>

{#await session}
	<Loading />
{:then _}
	<Router {routes} />
{:catch error}
	<Error
		code="503"
		description={error}
	>
		<button
			slot="actions"
			type="button"
			on:click={_ => session = setupSession()}
			class="mt-8 rounded-md border-2 dark:text-white dark:hover:bg-gray-700 dark:bg-gray-900 border-gray-300 dark:border-gray-700 shadow-sm px-4 py-2 bg-white text-base font-medium text-gray-700 hover:bg-gray-50 focus:outline-none"
		>
			Retry <Icon data={refresh} size={1.5} />
		</button>
	</Error>
{/await}

<style global>
	@tailwind base;
	@tailwind components;
	@tailwind utilities;
</style>