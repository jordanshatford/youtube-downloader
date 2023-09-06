<script lang="ts">
	import Toast from './Toast.svelte';
	import { toast as toasts, position as toastPos } from './stores';
	import { scale } from 'svelte/transition';
	import { flip } from 'svelte/animate';
	import { DEFAULT_ANIMATION, objectMerge } from './utils';
	import type { ToastPosition, ToastAnimation } from './types';

	/**
	 * The position of the toasts.
	 *
	 * The will also effect how the toasts stack on each other.
	 */
	export let position: ToastPosition = 'bottom-right';

	/** The animation properties. */
	export let animation: ToastAnimation | undefined = undefined;

	$toastPos = position;
	const ANIMATION = objectMerge(DEFAULT_ANIMATION, animation);
</script>

<div class="yd-toast-container" data-position={position}>
	{#each $toasts as toast (toast.id)}
		<div
			class="yd-toast-wrapper"
			data-position={position}
			in:scale={{
				start: ANIMATION.start,
				opacity: ANIMATION.opacity,
				duration: ANIMATION.duration
			}}
			out:scale={{ duration: ANIMATION.duration }}
			animate:flip={{ duration: ANIMATION.duration }}
		>
			<Toast {toast} />
		</div>
	{/each}
</div>

<style>
	.yd-toast-container {
		position: fixed;
		padding: var(--yd-toast-offset, 16px);
		top: 0;
		height: 100%;
		width: 100%;
		pointer-events: none;
		z-index: 999;
		display: flex;
		flex-direction: column;
		gap: var(--yd-toast-gap, 16px);
		overflow: hidden;
	}
	.yd-toast-container[data-position*='center'] {
		align-items: center;
	}
	.yd-toast-container[data-position*='bottom'] {
		justify-content: flex-end;
	}
	.yd-toast-container[data-position*='center'] {
		left: 50%;
		transform: translateX(-50%);
	}
	.yd-toast-container[data-position*='-left'] {
		left: 0;
		align-items: flex-start;
	}
	.yd-toast-container[data-position*='-right'] {
		right: 0;
		align-items: flex-end;
	}
	.yd-toast-wrapper[data-position='bottom-center'] {
		transform-origin: bottom center;
	}
	.yd-toast-wrapper[data-position='bottom-left'] {
		transform-origin: bottom left;
	}
	.yd-toast-wrapper[data-position='bottom-right'] {
		transform-origin: bottom right;
	}
	.yd-toast-wrapper[data-position='top-center'] {
		transform-origin: top center;
	}
	.yd-toast-wrapper[data-position='top-left'] {
		transform-origin: top left;
	}
	.yd-toast-wrapper[data-position='top-right'] {
		transform-origin: top right;
	}
</style>
