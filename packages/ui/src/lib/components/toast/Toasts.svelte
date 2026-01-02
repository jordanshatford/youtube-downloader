<script lang="ts">
	import { onMount } from 'svelte';
	import { flip } from 'svelte/animate';
	import { scale } from 'svelte/transition';

	import type { ToastAnimation, ToastComponentOptions, ToastPosition } from './types';
	import { toasts } from './stores.svelte';
	import Toast from './Toast.svelte';
	import { DEFAULT_ANIMATION, DEFAULT_POSITION } from './utils';

	interface Props {
		position?: ToastPosition;
		options?: Partial<ToastComponentOptions> | undefined;
		/** The animation properties. */
		animation?: Partial<ToastAnimation> | undefined;
	}

	let { position = DEFAULT_POSITION, options = undefined, animation = undefined }: Props = $props();

	onMount(() => {
		toasts.position = position;
		toasts.options = { ...toasts.options, ...options };
	});
	let _animation = $derived({ ...DEFAULT_ANIMATION, ...animation });
</script>

<div
	class="pointer-events-none fixed top-0 z-999 flex h-full w-full flex-col gap-y-1 overflow-hidden p-4 data-[position*=bottom]:justify-end data-[position*=center]:left-2/4 data-[position*=center]:-translate-x-2/4 data-[position*=center]:items-center data-[position*=left]:left-0 data-[position*=left]:items-start data-[position*=right]:right-0 data-[position*=right]:items-end"
	data-position={toasts.position}
>
	{#each toasts.toasts as toast (toast.id)}
		<div
			class="data-[position=bottom-center]:origin-bottom data-[position=bottom-left]:origin-bottom-left data-[position=bottom-right]:origin-bottom-right data-[position=top-center]:origin-top data-[position=top-left]:origin-top-left data-[position=top-right]:origin-top-right"
			data-position={toasts.position}
			in:scale={{
				start: _animation.start,
				opacity: _animation.opacity,
				duration: _animation.duration
			}}
			out:scale={{ duration: _animation.duration }}
			animate:flip={{ duration: _animation.duration }}
		>
			<Toast {toast} />
		</div>
	{/each}
</div>
