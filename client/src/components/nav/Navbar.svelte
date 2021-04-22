<script lang="ts">
    import { routeIsActive, navigateTo } from 'svelte-router-spa'
    import { download } from "svelte-awesome/icons"
    import { downloadsStore } from "../../stores/downloads"
    import NavbarItem from "./NavbarItem.svelte"
    import NavbarIcon from "./NavbarIcon.svelte"
    import Hamburger from "./mobile/Hamburger.svelte"
    import MobileMenu from "./mobile/MobileMenu.svelte"

    export let currentRoute: string

    let menuOpen = false

    let routes = [
        {
            label: "Search Videos",
            path: "/search",
        },
        {
            label: "Downloads",
            path: "/downloads",
        }
    ]

    $: downloadsPageActive = currentRoute && routeIsActive("/downloads", true);
</script>

<nav class="bg-gray-800 mb-4">
    <div class="max-w-7xl mx-auto px-2 sm:px-6 lg:px-8">
        <div class="relative flex items-center justify-between h-16">
            <Hamburger on:click={_ => menuOpen = !menuOpen} isOpen={menuOpen} />
            <div class="flex-1 flex items-center justify-center sm:items-stretch sm:justify-start">
                <div class="flex-shrink-0 flex items-center">
                    <img class="block h-8 w-auto" src="images/logo.png" alt="Logo">
                </div>
                <div class="hidden sm:block sm:ml-6">
                    <div class="flex space-x-4">
                        {#each routes as route}
                        <NavbarItem {route} currentRoute={currentRoute} />
                        {/each}
                    </div>
                </div>
            </div>
            <div class="absolute inset-y-0 right-0 flex items-center space-x-4 pr-2 sm:static sm:inset-auto sm:ml-6 sm:pr-0">
                <NavbarIcon on:click={_ => navigateTo("/downloads")} active={downloadsPageActive} data={download} notifications={Object.keys($downloadsStore).length} />
            </div>
        </div>
    </div>
    <MobileMenu isOpen={menuOpen} {routes} {currentRoute}/>
</nav>
  