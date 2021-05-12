<script lang="ts">
    import NavbarItem from "../NavbarItem.svelte"

    export let currentRoute: string
    export let routes: any[]
    export let isOpen: boolean
</script>

<div class="sm:hidden">
    {#if isOpen}
        <div class="px-2 pt-2 pb-3 space-y-1">
            {#each routes as route}
                <NavbarItem route={route} currentRoute={currentRoute} dropdown={true} />
            {/each}
        </div>
    {/if}
</div>