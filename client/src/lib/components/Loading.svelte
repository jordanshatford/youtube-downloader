<script lang="ts">
	import Spinner from '$lib/components/Spinner.svelte'
</script>

<div class="bg-white dark:bg-gray-900">
	<div class="flex h-screen">
		<div class="m-auto text-center">
			<div class="inline-block relative w-100 overflow-hidden align-middle">
				<div class="text-gray-900 dark:text-white">
					<Spinner className="mt-8" size={7} />
					<img class="absolute inset-4 mt-8 h-20 w-auto" src="images/logo.png" alt="Logo" />
				</div>
			</div>
		</div>
	</div>
</div>
