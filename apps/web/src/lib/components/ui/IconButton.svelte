<script lang="ts">
	import type { PlusIcon } from '@yd/ui';

	export let icon: typeof PlusIcon;
	export let size = '1x';
	let className = '';
	export { className as class };
</script>

<button on:click class="{className} border-none focus:outline-none p-2">
	<svelte:component this={icon} {size} />
</button>
