<script lang="ts">
    import { routeIsActive, Navigate } from "svelte-router-spa"
    import Icon from "../Icon.svelte"

    export let route: any
    export let currentRoute: string
    export let dropdown = false

    $: isActive = currentRoute && route.path && routeIsActive(route.path, true);
</script>
  
<Navigate
    to={route.path}
    title={route.label}
    styles="{isActive ? "bg-gray-50 dark:bg-gray-800" : "dark:bg-gray-900"} hover:bg-gray-50 dark:hover:bg-gray-700 text-gray-500 dark:text-gray-200 hover:text-gray-700 {dropdown ? 'block' : ''} px-3 py-2 rounded-md text-sm font-medium"
>
    <Icon data={route.icon} className="mb-1 mr-1" size={1.4} /> {route.label}
</Navigate>
