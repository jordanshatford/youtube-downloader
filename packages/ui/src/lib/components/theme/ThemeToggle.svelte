<script lang="ts">
	import IconButton from '../IconButton.svelte';
	import { MoonIcon, SunIcon } from '../../icons';
	import { theme } from './store';
</script>

<IconButton
	on:click={() => theme.toggle()}
	src={$theme === 'dark' ? SunIcon : MoonIcon}
	class="h-10 w-10 text-zinc-500 hover:text-brand-600 dark:bg-zinc-800 dark:text-zinc-200 dark:hover:text-brand-600"
/>
