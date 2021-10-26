<script lang="ts">
	import IconButton from '$lib/components/IconButton.svelte'
	import { theme } from '$lib/stores/theme'
	import { moon, sun } from '$lib/components/icons'
</script>

<IconButton
	on:click={() => theme.toggle()}
	data={$theme === 'dark' ? sun : moon}
	className="text-gray-500 dark:text-gray-200 dark:bg-gray-900 hover:bg-gray-50 dark:hover:bg-gray-800 hover:text-gray-700"
	size={1.5}
/>
