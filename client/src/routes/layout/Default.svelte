<script lang="ts">
    import { Route } from "svelte-router-spa"
    import Navbar from "../../lib/nav/Navbar.svelte"

    export let currentRoute: any
</script>

<div class="dark:bg-gray-900">
    <Navbar currentRoute={currentRoute} />
    <main class="min-h-screen dark:bg-gray-900 max-w-7xl mt-8 mx-auto px-4 sm:px-6 lg:px-8">
        <Route {currentRoute} />
    </main>
</div>