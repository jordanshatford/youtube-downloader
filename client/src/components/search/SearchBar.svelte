<script>
    import Icon from "svelte-awesome"
    import { circleONotch, search } from "svelte-awesome/icons"
    import { createEventDispatcher } from "svelte"
    import { DEFAULT_RESULT_SIZE, MAX_VIDEO_RESULTS } from "../../utils/constants.js"
    const dispatch = createEventDispatcher();

    export let disabled = false

    let searchTerm
    let numberResults = DEFAULT_RESULT_SIZE

    function dispatchSearch(event) {
        if (event.key === 'Enter' && searchTerm.length > 0) {
            dispatch("search", {
                searchTerm,
                numberResults
            })
        }
    }
</script>

<div class="max-w-xl mx-auto rounded-lg overflow-hidden md:max-w-xl">
    <div class="md:flex">
        <div class="w-full p-3">
            <div class="relative">
                {#if disabled}
                <Icon data={circleONotch} spin class="absolute text-gray-400 top-5 left-4" />
                {:else}
                <Icon data={search} class="absolute text-gray-400 top-5 left-4" /> 
                {/if}
                <input {disabled} bind:value={searchTerm} on:keypress={dispatchSearch} type="text" class="bg-white h-14 w-full px-12 rounded-lg focus:outline-none hover:cursor-pointer" name=""> 
                <span class="absolute top-4 right-5 border-l pl-4">
                    <select {disabled} bind:value={numberResults} class="focus:outline-none border-none text-gray-500 hover:cursor">
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