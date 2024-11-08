<script lang="ts">
	import { MoonIcon, SunIcon } from '../../icons';
	import IconButton from '../IconButton.svelte';
	import { theme } from './store';
</script>

<IconButton
	onclick={() => theme.toggle()}
	src={$theme === 'dark' ? SunIcon : MoonIcon}
	class="h-6 w-6 text-zinc-500 hover:text-brand-600 dark:bg-zinc-800 dark:text-zinc-200 dark:hover:text-brand-600"
/>
