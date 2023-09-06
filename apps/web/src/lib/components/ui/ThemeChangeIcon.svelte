<script lang="ts">
	import IconButton from '$lib/components/ui/IconButton.svelte';
	import { MoonIcon, SunIcon } from '@yd/ui';
	import { theme } from '$lib/stores/theme';

	let className = '';
	export { className as class };
	export let size = '1.5x';
</script>

<IconButton
	on:click={() => theme.toggle()}
	icon={$theme === 'dark' ? SunIcon : MoonIcon}
	class="{className} hover:text-indigo-800 dark:hover:text-indigo-600 text-zinc-500 dark:text-zinc-200 dark:bg-zinc-800"
	{size}
/>
