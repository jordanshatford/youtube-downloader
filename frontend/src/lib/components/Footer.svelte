<script lang="ts">
	import { GithubIcon } from 'svelte-feather-icons'
	import { RoutePathConstants } from '$lib/utils/route'
</script>

<footer class="bg-white dark:bg-gray-800 border-t border-gray-200 dark:border-gray-900">
	<div class="flex flex-col items-center px-8 py-6 mx-auto max-w-6xl sm:flex-row">
		<p class="text-gray-400">© 2021 {RoutePathConstants.PUBLIC_HOST_NAME}</p>
		<span
			class="inline-flex justify-end mt-4 space-x-5 sm:ml-auto sm:mt-0 sm:justify-start text-gray-500 dark:text-gray-200"
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
				href={RoutePathConstants.GITHUB}
				class="text-2xl hover:text-indigo-800 dark:hover:text-indigo-600 text-gray-500 dark:text-gray-200"
				target="_blank"
			>
				<GithubIcon size="1x" />
			</a>
		</span>
	</div>
</footer>
