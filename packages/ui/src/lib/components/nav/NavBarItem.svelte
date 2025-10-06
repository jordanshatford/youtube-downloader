<script lang="ts">
	import type { RouteId } from '$app/types';
	import type { HTMLAnchorAttributes } from 'svelte/elements';
	import { resolve } from '$app/paths';

	import type { IconSource } from '../../icons';
	import { Icon } from '../../icons';

	interface Props extends HTMLAnchorAttributes {
		link: { href: RouteId; text: string; icon?: IconSource };
		activeLink: string;
		isMobileMenu?: boolean;
	}

	let { link, activeLink, isMobileMenu = false, ...rest }: Props = $props();

	let classNames = $derived(
		activeLink === link.href
			? 'text-zinc-700 dark:text-white bg-zinc-100 dark:bg-zinc-900'
			: 'text-zinc-400 dark:text-zinc-300 hover:bg-zinc-100 dark:hover:bg-zinc-700'
	);
</script>

<a
	{...rest}
	href={resolve(link.href)}
	class:block={isMobileMenu}
	class="{classNames} flex flex-row items-center rounded-lg px-3 py-2"
>
	{#if link.icon}
		<Icon src={link.icon} theme="solid" class="h-6 w-6 pr-2" />
	{/if}
	{link.text}
</a>
