<script lang="ts">
    import { Route } from "svelte-router-spa"

    import Navbar from "../../components/nav/Navbar.svelte"

    export let currentRoute: any
</script>
  
<div>
    <Navbar currentRoute={currentRoute} />
    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <Route {currentRoute} />
    </main>
</div>