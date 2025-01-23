<script lang="ts">
	import { MoonIcon, SunIcon } from '../../icons';
	import IconButton from '../IconButton.svelte';
	import { theme } from './store.svelte';
</script>

<IconButton
	onclick={() => theme.toggle()}
	src={theme.isDark ? SunIcon : MoonIcon}
	class="hover:text-brand-600 dark:hover:text-brand-600 h-6 w-6 text-zinc-500 hover:cursor-pointer dark:bg-zinc-800 dark:text-zinc-200"
/>
