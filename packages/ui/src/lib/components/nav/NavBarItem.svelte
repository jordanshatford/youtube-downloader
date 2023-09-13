<script lang="ts">
	export let link: { href: string; text: string };
	export let activeLink: string;
	export let isMobileMenu = false;

	$: classNames =
		activeLink === link.href
			? 'text-zinc-700 dark:text-white bg-zinc-100 dark:bg-zinc-900'
			: 'text-zinc-400 dark:text-zinc-300 hover:bg-zinc-100 dark:hover:bg-zinc-700';
</script>

<a on:click href={link.href} class:block={isMobileMenu} class="{classNames} rounded-lg px-3 py-2">
	{link.text}
</a>
