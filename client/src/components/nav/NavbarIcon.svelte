<script>
    import Icon from "svelte-awesome"
    import { createEventDispatcher } from "svelte"

    const dispatch = createEventDispatcher();

    export let data
    export let notifications
    export let active
</script>

<span class="relative inline-block">
    <button on:click={_ => dispatch("click")} class="{active ? 'bg-gray-900 text-white' : 'text-gray-300 hover:bg-gray-700 hover:text-white'} p-1 rounded-md border-none focus:outline-none">
        <Icon {data} class="h-6 w-6" />
    </button>
    {#if notifications > 0}
    <span class="absolute top-0 right-0 inline-flex items-center justify-center px-2 py-1 text-xs font-bold leading-none text-white transform translate-x-1/2 -translate-y-1/2 bg-red-600 rounded-full">
        { notifications }
    </span>
    {/if}
</span>
