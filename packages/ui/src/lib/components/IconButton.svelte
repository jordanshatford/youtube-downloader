<script lang="ts">
	import type { HTMLButtonAttributes } from 'svelte/elements';
	import { Icon, type IconSource } from '../icons';

	interface $$Props extends HTMLButtonAttributes {
		src: IconSource;
		theme?: string;
	}

	export let src: $$Props['src'];
	export let theme: $$Props['theme'] = undefined;
</script>

<button
	on:click
	{...$$restProps}
	type="button"
	class="border-none p-2 focus:outline-none {$$props.class}"
>
	<Icon {src} {theme} />
</button>
