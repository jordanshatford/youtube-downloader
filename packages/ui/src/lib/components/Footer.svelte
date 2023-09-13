<script lang="ts">
	import { GithubIcon, Icon } from '../icons';

	export let githubLink: string | undefined = undefined;
	export let copyright: { owner: string; year: number } | undefined = undefined;
	export let links: { href: string; text: string }[] = [];
</script>

<footer class="border-t border-zinc-200 bg-white dark:border-zinc-900 dark:bg-zinc-800">
	<div class="mx-auto flex max-w-6xl flex-col items-center px-8 py-6 sm:flex-row">
		{#if copyright}
			<p class="text-zinc-400">© {copyright.year} {copyright.owner}</p>
		{/if}
		<span
			class="mt-4 inline-flex justify-end space-x-5 text-zinc-500 dark:text-zinc-200 sm:ml-auto sm:mt-0 sm:justify-start"
		>
			{#each links as link, index (link.href)}
				{@const isLast = index === links.length - 1}
				<a href={link.href} class="hover:text-indigo-800 dark:hover:text-indigo-600">
					{link.text}
				</a>
				{#if !isLast}
					<span> - </span>
				{/if}
			{/each}
		</span>
		<span class="mt-4 inline-flex justify-center space-x-5 sm:ml-auto sm:mt-0 sm:justify-start">
			{#if githubLink}
				<a
					href={githubLink}
					class="text-2xl text-zinc-500 hover:text-indigo-800 dark:text-zinc-200 dark:hover:text-indigo-600"
					target="_blank"
					rel="noreferrer"
				>
					<Icon src={GithubIcon} class="h-6 w-6" />
				</a>
			{/if}
		</span>
	</div>
</footer>
