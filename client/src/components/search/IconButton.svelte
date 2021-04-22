<script lang="ts">
    import Icon from "svelte-awesome"
    
    export let data: any
</script>

<button on:click class="px-4 py-2 rounded-full shadow hover:shadow-md outline-none focus:outline-none mr-1 mb-2 ease-linear transition-all duration-150" type="button">
    <Icon data={data} class="text-gray-400" /> 
</button>