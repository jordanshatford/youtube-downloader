<script lang="ts">
    import Icon from "svelte-awesome"
    import { routeIsActive, Navigate } from "svelte-router-spa"
    import type { Route } from "../../utils/types"

    export let route: Route
    export let currentRoute: string
    export let dropdown = false

    $: isActive = currentRoute && route.path && routeIsActive(route.path, true);
</script>
  
<Navigate
    to={route.path}
    title={route.label}
    styles="{isActive ? 'bg-gray-900 text-white' : 'text-gray-300 hover:bg-gray-700 hover:text-white'} {dropdown ? 'block' : ''} px-3 py-2 rounded-md text-sm font-medium"
>
    <Icon data={route.icon} class="mb-1 mr-1" /> {route.label}
</Navigate>
