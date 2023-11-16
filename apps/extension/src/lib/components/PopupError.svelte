<script lang="ts">
	export let message: string = 'Unexpected error!';
</script>

<div class="flex h-full flex-col items-center justify-center space-y-2 text-center">
	<h1 class="text-3xl font-black text-gray-300 dark:text-gray-600">Error</h1>
	<p class="mt-2 text-gray-500 dark:text-gray-400">{message}</p>
</div>
