<script lang="ts">
    import { createEventDispatcher } from "svelte"
    import Icon from "../Icon.svelte"
    import Spinner from "../Spinner.svelte"
    import { search } from "../icons"
    import { MAX_VIDEO_RESULTS } from "../../utils/constants"

    const dispatch = createEventDispatcher();

    export let disabled = false

    export let searchTerm: string
    export let numberResults: number

    function dispatchSearch(event: KeyboardEvent) {
        if (event.key === 'Enter' && searchTerm.length > 0) {
            dispatch("search", {
                searchTerm,
                numberResults
            })
        }
    }
</script>

<div class="max-w-xl mx-auto rounded-lg overflow-hidden md:max-w-xl mt-4">
    <div class="md:flex">
        <div class="w-full p-3">
            <div class="relative">
                {#if disabled}
                <Spinner className="absolute text-gray-400 top-10 left-4" />
                {:else}
                <Icon data={search} className="absolute text-gray-400 top-10 left-4" />
                {/if}
                <input
                    {disabled}
                    bind:value={searchTerm}
                    on:keypress={dispatchSearch}
                    type="text"
                    class="border border-gray-400 bg-white disabled:text-gray-200 h-14 w-full px-12 rounded-lg focus:outline-none hover:cursor-pointer"
                    name=""
                >
                <span class="absolute top-10 right-5 border-l pl-4">
                    <select {disabled} bind:value={numberResults} class="disabled:text-gray-200 focus:outline-none border-none text-gray-500 hover:cursor">
                        {#each {length: MAX_VIDEO_RESULTS} as _, i}
                            <option value={i+1}>
                                {i+1}
                            </option>
                        {/each}
                    </select>
                </span>
            </div>
        </div>
    </div>
</div>