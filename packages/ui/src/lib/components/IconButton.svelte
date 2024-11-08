<script lang="ts">
	import type { HTMLButtonAttributes } from 'svelte/elements';

	import type { IconSource } from '../icons';
	import { Icon } from '../icons';

	interface Props extends HTMLButtonAttributes {
		src: IconSource;
		theme?: string;
	}

	let { src, theme = undefined, ...rest }: Props = $props();
</script>

<button {...rest} type="button">
	<Icon {src} {theme} />
</button>
