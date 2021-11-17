<script lang="ts">
	import IconButton from '$lib/components/ui/IconButton.svelte'
	import { MoonIcon, SunIcon } from 'svelte-feather-icons'
	import { theme } from '$lib/stores/theme'

	let className = ''
	export { className as class }
	export let size = '1.5x'
</script>

<IconButton
	on:click={() => theme.toggle()}
	icon={$theme === 'dark' ? SunIcon : MoonIcon}
	class="{className} hover:text-indigo-800 dark:hover:text-indigo-600 text-gray-500 dark:text-gray-200 dark:bg-gray-800"
	{size}
/>
