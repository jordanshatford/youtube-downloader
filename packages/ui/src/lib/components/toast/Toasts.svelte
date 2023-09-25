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

<div
	class="pointer-events-none fixed top-0 z-[999] flex h-full w-full flex-col gap-y-1 overflow-hidden p-[16px] data-[position*=center]:left-2/4 data-[position*=left]:left-0 data-[position*=right]:right-0 data-[position*=center]:-translate-x-2/4 data-[position*=left]:items-start data-[position*=right]:items-end data-[position*=center]:items-center data-[position*=bottom]:justify-end"
	data-position={position}
>
	{#each $toasts as toast (toast.id)}
		<div
			class="data-[position=bottom-center]:origin-bottom data-[position=bottom-left]:origin-bottom-left data-[position=bottom-right]:origin-bottom-right data-[position=top-center]:origin-top data-[position=top-left]:origin-top-left data-[position=top-right]:origin-top-right"
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
