<script lang="ts">
	import { RoutePathConstants } from '$lib/routes';

	export let title: string = '404';
	export let subtitle: string = '';
	export let description: string = "We can't find that page.";
</script>

<div class="-mt-16 grid h-screen place-content-center px-4">
	<div class="text-center">
		<h1 class="text-7xl font-black text-gray-300 dark:text-gray-600">{title}</h1>
		<p class="text-2xl font-bold tracking-tight text-gray-900 dark:text-white sm:text-4xl">
			{subtitle}
		</p>
		<p class="mt-2 text-gray-500 dark:text-gray-400">
			{description}
		</p>
		<a
			href={RoutePathConstants.SEARCH}
			class="mt-6 inline-block rounded bg-brand-600 px-5 py-3 text-sm font-medium text-white hover:opacity-90 focus:outline-none"
		>
			Go back to search
		</a>
	</div>
</div>
