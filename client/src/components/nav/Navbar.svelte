<script>
    import NavbarItem from "./NavbarItem.svelte"
    import NavbarIcon from "./NavbarIcon.svelte"
    import Hamburger from "./mobile/Hamburger.svelte"
    import MobileMenu from "./mobile/MobileMenu.svelte"

    export let currentRoute

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
            <NavbarIcon />
        </div>
    </div>
    <MobileMenu isOpen={menuOpen} {routes} {currentRoute}/>
</nav>
  