<script>
    import Icon from 'svelte-awesome'
	import { createEventDispatcher } from "svelte";

    const dispatch = createEventDispatcher();
    
    export let data
    
    function handleClick() {
        dispatch("click")
    }
</script>

<button on:click={handleClick} class="px-4 py-2 rounded-full shadow hover:shadow-md outline-none focus:outline-none mr-1 mb-2 ease-linear transition-all duration-150" type="button">
    <Icon data={data} class="text-gray-400" /> 
</button>