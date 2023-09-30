<script lang="ts">
	import { Icon, LoaderIcon, type IconSource } from '../icons';

	export let src: IconSource;
	export let disabled: boolean = false;
	export let loading: boolean = false;
</script>

<button
	{...$$restProps}
	class="inline-block p-3 text-zinc-700 hover:bg-zinc-50 focus:relative disabled:opacity-25 dark:text-zinc-200 dark:hover:bg-zinc-800"
	disabled={disabled || loading}
	on:click
>
	<Icon src={loading ? LoaderIcon : src} class="h-4 w-4 {loading && 'animate-spin'}" />
</button>
