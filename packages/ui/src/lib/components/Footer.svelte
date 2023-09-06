<script lang="ts">
	import { GithubIcon } from '../icons';
	import type { LinkInfo } from '../types';

	export let githubLink: string | undefined = undefined;
	export let copyright: { owner: string; year: number } | undefined = undefined;
	export let links: LinkInfo[] = [];
</script>

<footer class="bg-white dark:bg-zinc-800 border-t border-zinc-200 dark:border-zinc-900">
	<div class="flex flex-col items-center px-8 py-6 mx-auto max-w-6xl sm:flex-row">
		{#if copyright}
			<p class="text-zinc-400">© {copyright.year} {copyright.owner}</p>
		{/if}
		<span
			class="inline-flex justify-end mt-4 space-x-5 sm:ml-auto sm:mt-0 sm:justify-start text-zinc-500 dark:text-zinc-200"
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
		<span class="inline-flex justify-center mt-4 space-x-5 sm:ml-auto sm:mt-0 sm:justify-start">
			{#if githubLink}
				<a
					href={githubLink}
					class="text-2xl hover:text-indigo-800 dark:hover:text-indigo-600 text-zinc-500 dark:text-zinc-200"
					target="_blank"
					rel="noreferrer"
				>
					<GithubIcon size="1x" />
				</a>
			{/if}
		</span>
	</div>
</footer>
