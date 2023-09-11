<script lang="ts">
	import type { PlusIcon } from '../icons';

	export let icon: typeof PlusIcon;
	export let size = '1x';
	let className = '';
	export { className as class };
</script>

<button on:click class="{className} border-none p-2 focus:outline-none">
	<svelte:component this={icon} {size} />
</button>
