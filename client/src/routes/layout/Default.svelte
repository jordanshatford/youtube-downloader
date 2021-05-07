<script lang="ts">
    import { onMount } from "svelte"
    import { Route } from "svelte-router-spa"
    import { theme } from "../../stores/theme"
    import Navbar from "../../lib/nav/Navbar.svelte"

    export let currentRoute: any

    onMount(() => {
        if ($theme === "dark") {
            document.querySelector("html").classList.add("dark")
        }
    })
</script>

<div class="dark:bg-gray-900">
    <Navbar currentRoute={currentRoute} />
    <main class="min-h-screen dark:bg-gray-900 max-w-7xl mt-8 mx-auto px-4 sm:px-6 lg:px-8">
        <Route {currentRoute} />
    </main>
</div>