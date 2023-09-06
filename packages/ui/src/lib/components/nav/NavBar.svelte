<script lang="ts">
	import { MenuIcon, XIcon } from '../../icons';
	import IconButton from '../IconButton.svelte';
	import type { LinkInfo } from '../../types';
	import NavBarItem from './NavBarItem.svelte';

	let showMobileMenu = false;

	export let links: LinkInfo[];
</script>

<nav class="bg-white dark:bg-zinc-800 shadow dark:shadow-dark fixed top-0 z-40 w-full">
	<div class="max-w-7xl mx-auto px-2 sm:px-6 lg:px-8">
		<div class="relative flex items-center justify-between h-16">
			<div class="absolute inset-y-0 left-0 flex items-center sm:hidden">
				<IconButton
					on:click={() => (showMobileMenu = !showMobileMenu)}
					class="{showMobileMenu
						? 'hover:text-red-600'
						: 'hover:text-indigo-800 dark:hover:text-indigo-600'} dark:text-zinc-200"
					icon={showMobileMenu ? XIcon : MenuIcon}
					size="1.5x"
				/>
			</div>
			<div class="flex-1 flex items-center justify-center sm:items-stretch sm:justify-start">
				<div class="flex-shrink-0 flex items-center">
					<slot name="logo" />
				</div>
				<div class="hidden sm:block sm:ml-6">
					<div class="flex space-x-4">
						{#each links as link (link.href)}
							<NavBarItem {link} />
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
			<div class="px-2 pt-2 pb-3 space-y-1">
				{#each links as link (link.href)}
					<NavBarItem on:click={() => (showMobileMenu = false)} {link} isMobileMenu />
				{/each}
			</div>
		</div>
	{/if}
</nav>
