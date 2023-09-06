<script lang="ts">
	import { page } from '$app/stores';
	import type { LinkInfo } from '../../types';

	export let link: LinkInfo;
	export let isMobileMenu = false;

	$: classNames =
		$page.url.pathname === link.href
			? 'text-zinc-700 dark:text-white bg-zinc-100 dark:bg-zinc-900'
			: 'text-zinc-400 dark:text-zinc-300 hover:bg-zinc-100 dark:hover:bg-zinc-700';
</script>

<a on:click href={link.href} class:block={isMobileMenu} class="{classNames} px-3 py-2 rounded-lg">
	{link.text}
</a>
