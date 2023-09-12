<script lang="ts">
	import { MenuIcon, XMarkIcon } from '../../icons';
	import IconButton from '../IconButton.svelte';
	import type { LinkInfo } from '../../types';
	import NavBarItem from './NavBarItem.svelte';

	let showMobileMenu = false;

	export let links: LinkInfo[];
	export let activeLink: string;
</script>

<nav class="fixed top-0 z-40 w-full bg-white shadow dark:bg-zinc-800 dark:shadow-dark">
	<div class="mx-auto max-w-7xl px-2 sm:px-6 lg:px-8">
		<div class="relative flex h-16 items-center justify-between">
			<div class="absolute inset-y-0 left-0 flex items-center sm:hidden">
				<IconButton
					on:click={() => (showMobileMenu = !showMobileMenu)}
					class="{showMobileMenu
						? 'hover:text-red-600'
						: 'hover:text-indigo-800 dark:hover:text-indigo-600'} h-10 w-10 dark:text-zinc-200"
					src={showMobileMenu ? XMarkIcon : MenuIcon}
				/>
			</div>
			<div class="flex flex-1 items-center justify-center sm:items-stretch sm:justify-start">
				<div class="flex flex-shrink-0 items-center">
					<slot name="logo" />
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
				<slot name="right" />
			</div>
		</div>
	</div>
	{#if showMobileMenu}
		<div>
			<div class="space-y-1 px-2 pb-3 pt-2">
				{#each links as link (link.href)}
					<NavBarItem on:click={() => (showMobileMenu = false)} {link} {activeLink} isMobileMenu />
				{/each}
			</div>
		</div>
	{/if}
</nav>
