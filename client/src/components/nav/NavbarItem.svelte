<script>
    import { routeIsActive, Navigate } from "svelte-router-spa"
  
    export let route
    export let currentRoute
    export let dropdown = false

    $: isActive = currentRoute && route.path && routeIsActive(route.path, true);
</script>
  
<Navigate
    to={route.path}
    title={route.label}
    styles="{isActive ? 'bg-gray-900 text-white' : 'text-gray-300 hover:bg-gray-700 hover:text-white'} {dropdown ? 'block' : ''} px-3 py-2 rounded-md text-sm font-medium"
>
    {route.label}
</Navigate>
