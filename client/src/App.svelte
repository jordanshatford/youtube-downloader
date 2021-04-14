<script>
	import { Router } from 'svelte-router-spa'
  	import { routes } from './routes'
</script>

<main>
	<div class="py-12 bg-white">
		<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
			<Router {routes} />
		</div>
	</div>  
</main>

<style global>
	@tailwind base;
	@tailwind components;
	@tailwind utilities;
</style>