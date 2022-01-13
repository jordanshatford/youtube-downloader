<script lang="ts">
	import { GithubIcon } from 'svelte-feather-icons'
	import { RoutePathConstants } from '$lib/utils/route'
	import config from '$lib/config'
</script>

<footer class="bg-white dark:bg-zinc-800 border-t border-zinc-200 dark:border-zinc-900">
	<div class="flex flex-col items-center px-8 py-6 mx-auto max-w-6xl sm:flex-row">
		<p class="text-zinc-400">© {config.app.year} {config.app.creator}</p>
		<span
			class="inline-flex justify-end mt-4 space-x-5 sm:ml-auto sm:mt-0 sm:justify-start text-zinc-500 dark:text-zinc-200"
		>
			<a href={RoutePathConstants.FAQ} class="hover:text-indigo-800 dark:hover:text-indigo-600">
				faq
			</a>
			<span> - </span>
			<a
				href={RoutePathConstants.TERMS_OF_USE}
				class="hover:text-indigo-800 dark:hover:text-indigo-600"
			>
				terms of use
			</a>
		</span>
		<span class="inline-flex justify-center mt-4 space-x-5 sm:ml-auto sm:mt-0 sm:justify-start">
			<a
				href={config.app.github}
				class="text-2xl hover:text-indigo-800 dark:hover:text-indigo-600 text-zinc-500 dark:text-zinc-200"
				target="_blank"
			>
				<GithubIcon size="1x" />
			</a>
		</span>
	</div>
</footer>
