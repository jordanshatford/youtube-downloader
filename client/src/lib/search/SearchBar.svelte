<script lang="ts">
    import { createEventDispatcher } from "svelte"
    import Icon from "../Icon.svelte"
    import Spinner from "../Spinner.svelte"
    import { search } from "../icons"

    const dispatch = createEventDispatcher();

    export let loading = false

    export let searchTerm: string

    function dispatchSearch(event: KeyboardEvent) {
        if (event.key === 'Enter' && searchTerm.length > 0) {
            dispatch("search", { term: searchTerm })
        }
    }
</script>

<div class="max-w-xl mx-auto rounded-lg overflow-hidden md:max-w-xl mt-4">
    <div class="md:flex">
        <div class="w-full p-3">
            <div class="relative">
                {#if loading}
                    <Spinner className="absolute text-gray-400 top-10 left-4" />
                {:else}
                    <Icon data={search} className="absolute text-gray-400 top-10 left-4" />
                {/if}
                <input
                    disabled={loading}
                    bind:value={searchTerm}
                    on:keypress={dispatchSearch}
                    type="text"
                    class="border border-gray-400 bg-white disabled:text-gray-200 h-14 w-full px-12 rounded-lg focus:outline-none hover:cursor-pointer"
                    name=""
                >
            </div>
        </div>
    </div>
</div>