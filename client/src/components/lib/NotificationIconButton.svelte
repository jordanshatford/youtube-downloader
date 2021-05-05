<script lang="ts">
    import IconButton from "../lib/IconButton.svelte"

    export let data: any
    export let notifications: number
    export let active: boolean
</script>

<span class="relative inline-block">
    <IconButton 
        on:click
        {data}
        className="{active ? "bg-gray-50 dark:bg-gray-800" : "dark:bg-gray-900"} text-gray-500 dark:text-gray-200 hover:bg-gray-50 hover:text-gray-700 dark:hover:bg-gray-700"
        scale={1.5}
    />
    {#if notifications > 0}
    <span class="absolute top-0 right-0 inline-flex items-center justify-center px-2 py-1 text-xs font-bold leading-none text-white transform translate-x-1/2 -translate-y-1/2 bg-red-600 rounded-full">
        { notifications }
    </span>
    {/if}
</span>
