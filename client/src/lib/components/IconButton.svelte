<script lang="ts">
	import Icon from '$lib/components/Icon.svelte'

	export let data: string
	export let size = 1
	export let className = ''
</script>

<button on:click class="{className} rounded-md border-none focus:outline-none p-2" type="button">
	<Icon {data} {size} />
</button>
