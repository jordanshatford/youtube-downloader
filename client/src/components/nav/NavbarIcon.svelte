<script>
    import Icon from 'svelte-awesome'
    import { bell } from 'svelte-awesome/icons'

    let active = false
</script>

<div class="absolute inset-y-0 right-0 flex items-center pr-2 sm:static sm:inset-auto sm:ml-6 sm:pr-0">
    <button class="{active ? 'bg-gray-900 text-white' : 'text-gray-300 hover:bg-gray-700 hover:text-white'} p-1 rounded-md border-none focus:outline-none">
        <Icon data={bell} class="h-6 w-6" /> 
    </button>
</div>