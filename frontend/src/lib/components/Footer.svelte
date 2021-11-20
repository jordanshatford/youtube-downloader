<script lang="ts">
	import { GithubIcon } from 'svelte-feather-icons'
</script>

<footer class="bg-white dark:bg-gray-800 border-t border-gray-200 dark:border-gray-900">
	<div class="flex flex-col items-center px-8 py-6 mx-auto max-w-6xl sm:flex-row">
		<p class="text-sm text-gray-400 dark:text-gray-300">© 2021 Youtube to MP3</p>
		<span class="inline-flex justify-center mt-4 space-x-5 sm:ml-auto sm:mt-0 sm:justify-start">
			<a
				href="https://github.com/jordanshatford/youtube-to-mp3"
				class="text-2xl hover:text-indigo-800 dark:hover:text-indigo-600 text-gray-500 dark:text-gray-200"
				target="_blank"
			>
				<GithubIcon size="1x" />
			</a>
		</span>
	</div>
</footer>
