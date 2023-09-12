<script lang="ts">
	import { Icon, type IconSource } from '../icons';

	export let src: IconSource;
	export let theme: string | undefined = undefined;
	let className = '';
	export { className as class };
</script>

<button on:click class="{className} border-none p-2 focus:outline-none">
	<Icon {src} {theme} />
</button>
