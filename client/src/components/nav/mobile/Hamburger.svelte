<script lang="ts">
    import IconButton from "../../lib/IconButton.svelte"
    import { times, bars } from "svelte-awesome/icons"

    export let isOpen: boolean
</script>

<div class="absolute inset-y-0 left-0 flex items-center sm:hidden">
    <IconButton
        on:click
        data={isOpen ? times : bars}
        className="{isOpen ? "bg-gray-50 dark:bg-gray-800" : "dark:bg-gray-900"} text-gray-500 dark:text-gray-200 hover:bg-gray-50 dark:hover:bg-gray-800 hover:text-gray-700 inline-flex items-center justify-center"
        scale={1.5}
    />
</div>