<script lang="ts">
	import type { HTMLButtonAttributes } from 'svelte/elements';

	import type { IconSource } from '../icons';
	import { Icon, LoaderIcon } from '../icons';

	interface Props extends HTMLButtonAttributes {
		src: IconSource;
		disabled?: boolean;
		loading?: boolean;
	}

	let { src, disabled = false, loading = false, ...rest }: Props = $props();
</script>

<button
	{...rest}
	class="inline-block p-3 text-zinc-700 hover:bg-zinc-50 focus:relative disabled:opacity-25 dark:text-zinc-200 dark:hover:bg-zinc-800"
	disabled={disabled || loading}
>
	<Icon src={loading ? LoaderIcon : src} class="h-4 w-4 {loading && 'animate-spin'}" />
</button>
