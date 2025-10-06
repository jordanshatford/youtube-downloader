<script lang="ts">
	import type { RouteId } from '$app/types';
	import type { Snippet } from 'svelte';

	import type { IconSource } from '../../icons';
	import { MenuIcon, XMarkIcon } from '../../icons';
	import IconButton from '../IconButton.svelte';
	import NavBarItem from './NavBarItem.svelte';

	let showMobileMenu = $state(false);

	interface Props {
		links: { href: RouteId; text: string; icon?: IconSource }[];
		activeLink: string;
		logo?: Snippet;
		right?: Snippet;
	}

	let { links, activeLink, logo, right }: Props = $props();
</script>

<nav class="dark:shadow-dark fixed top-0 z-40 w-full bg-white shadow-sm dark:bg-zinc-800">
	<div class="mx-auto max-w-7xl px-2 sm:px-6 lg:px-8">
		<div class="relative flex h-16 items-center justify-between">
			<div class="absolute inset-y-0 left-0 flex items-center sm:hidden">
				<IconButton
					onclick={() => (showMobileMenu = !showMobileMenu)}
					class="{showMobileMenu
						? 'hover:text-red-600 dark:hover:text-red-600'
						: 'hover:text-brand-600 dark:hover:text-brand-600'} h-7 w-7 hover:cursor-pointer dark:text-zinc-200"
					src={showMobileMenu ? XMarkIcon : MenuIcon}
				/>
			</div>
			<div class="flex flex-1 items-center justify-center sm:items-stretch sm:justify-start">
				<div class="flex shrink-0 items-center">
					{@render logo?.()}
				</div>
				<div class="hidden sm:ml-6 sm:block">
					<div class="flex space-x-4">
						{#each links as link (link.href)}
							<NavBarItem {link} {activeLink} />
						{/each}
					</div>
				</div>
			</div>
			<div
				class="absolute inset-y-0 right-0 flex items-center pr-2 sm:static sm:inset-auto sm:ml-6 sm:pr-0"
			>
				{@render right?.()}
			</div>
		</div>
	</div>
	{#if showMobileMenu}
		<div>
			<div class="space-y-1 px-2 pt-2 pb-3">
				{#each links as link (link.href)}
					<NavBarItem onclick={() => (showMobileMenu = false)} {link} {activeLink} isMobileMenu />
				{/each}
			</div>
		</div>
	{/if}
</nav>
