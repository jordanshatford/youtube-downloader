<script lang="ts">
	import { GithubIcon, Icon } from '../icons';

	interface Props {
		githubLink?: string | undefined;
		copyright?: { owner: string; year: number } | undefined;
		links?: { href: string; text: string }[];
	}

	let { githubLink = undefined, copyright = undefined, links = [] }: Props = $props();
</script>

<footer class="border-t border-zinc-200 bg-white dark:border-zinc-900 dark:bg-zinc-800">
	<div class="mx-auto flex max-w-6xl flex-col items-center px-8 py-6 sm:flex-row">
		{#if copyright}
			<p class="text-zinc-400">© {copyright.year} {copyright.owner}</p>
		{/if}
		<span
			class="mt-4 inline-flex justify-end space-x-5 text-zinc-500 sm:mt-0 sm:ml-auto sm:justify-start dark:text-zinc-200"
		>
			{#each links as link, index (link.href)}
				{@const isLast = index === links.length - 1}
				<a href={link.href} class="hover:text-brand-600">
					{link.text}
				</a>
				{#if !isLast}
					<span> - </span>
				{/if}
			{/each}
		</span>
		<span class="mt-4 inline-flex justify-center space-x-5 sm:mt-0 sm:ml-auto sm:justify-start">
			{#if githubLink}
				<a
					href={githubLink}
					class="hover:text-brand-600 dark:hover:text-brand-600 text-2xl text-zinc-500 dark:text-zinc-200"
					target="_blank"
					rel="noreferrer"
					aria-label="See source code on GitHub"
				>
					<Icon src={GithubIcon} class="h-6 w-6" />
				</a>
			{/if}
		</span>
	</div>
</footer>
