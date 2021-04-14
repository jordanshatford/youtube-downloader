<script>
    import Icon from 'svelte-awesome'
    import { search } from 'svelte-awesome/icons'
	import { createEventDispatcher } from "svelte";

	const dispatch = createEventDispatcher();
    const MAX_VIDEO_RESULTS = 10

    export let allowResultSize = false
    let searchTerm
    let numberResults = 3

    function dispatchSearch(event) {
        if (event.key === 'Enter') {
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
                <Icon data={search} class="absolute text-gray-400 top-5 left-4" /> 
                <input bind:value={searchTerm} on:keypress={dispatchSearch} type="text" class="bg-white h-14 w-full px-12 rounded-lg focus:outline-none hover:cursor-pointer" name=""> 
                {#if allowResultSize}
                <span class="absolute top-4 right-5 border-l pl-4">
                    <select bind:value={numberResults} class="focus:outline-none border-none text-gray-500 hover:cursor">
                        {#each {length: MAX_VIDEO_RESULTS} as _, i}
                            <option value={i+1}>
                                {i+1}
                            </option>
                        {/each}
                    </select>
                </span>
                {/if}
            </div>
        </div>
    </div>
</div>