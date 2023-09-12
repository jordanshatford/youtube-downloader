<script lang="ts">
	import { MoonIcon, SunIcon, IconButton } from '@yd/ui';
	import { theme } from '$lib/stores/theme';

	let className = '';
	export { className as class };
</script>

<IconButton
	on:click={() => theme.toggle()}
	src={$theme === 'dark' ? SunIcon : MoonIcon}
	class="{className} h-10 w-10 text-zinc-500 hover:text-indigo-800 dark:bg-zinc-800 dark:text-zinc-200 dark:hover:text-indigo-600"
/>
