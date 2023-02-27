<script lang="ts">
	import type { SvelteComponent } from 'svelte';

	export let icon: typeof SvelteComponent;
	export let size = '1x';
	let className = '';
	export { className as class };
</script>

<button on:click class="{className} border-none focus:outline-none p-2">
	<svelte:component this={icon} {size} />
</button>
