<script>
    import { Route } from "svelte-router-spa"
    import Navbar from "../../components/nav/Navbar.svelte"

    export let currentRoute
</script>
  
<div class="app">
    <Navbar currentRoute={currentRoute} />
    <main>
        <Route {currentRoute} />
    </main>
</div>