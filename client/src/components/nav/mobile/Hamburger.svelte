<script lang="ts">
    import Icon from "svelte-awesome"
    import { times, bars } from "svelte-awesome/icons"

    export let isOpen: boolean
</script>

<div class="absolute inset-y-0 left-0 flex items-center sm:hidden">
    <button on:click type="button" class="{isOpen ? "bg-gray-900 text-white" : "text-gray-300 hover:bg-gray-700 hover:text-white" } inline-flex items-center justify-center p-2 rounded-md border-none focus:outline-none">
        <Icon data={isOpen ? times : bars} class="block h-6 w-6" /> 
    </button>
</div>