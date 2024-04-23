<script lang="ts">
	import { flip } from 'svelte/animate';
	import { scale } from 'svelte/transition';

	import type { ToastAnimation, ToastComponentOptions, ToastPosition } from './types';
	import { options as _options, position as _position, toast as toasts } from './stores';
	import Toast from './Toast.svelte';
	import { DEFAULT_ANIMATION, DEFAULT_POSITION } from './utils';

	export let position: ToastPosition = DEFAULT_POSITION;

	export let options: Partial<ToastComponentOptions> | undefined = undefined;

	/** The animation properties. */
	export let animation: Partial<ToastAnimation> | undefined = undefined;

	$_position = position;
	const OPTIONS = { ...$_options, ...options };
	$_options = OPTIONS;
	const ANIMATION = { ...DEFAULT_ANIMATION, ...animation };
</script>

<div
	class="pointer-events-none fixed top-0 z-[999] flex h-full w-full flex-col gap-y-1 overflow-hidden p-[16px] data-[position*=center]:left-2/4 data-[position*=left]:left-0 data-[position*=right]:right-0 data-[position*=center]:-translate-x-2/4 data-[position*=left]:items-start data-[position*=right]:items-end data-[position*=center]:items-center data-[position*=bottom]:justify-end"
	data-position={$_position}
>
	{#each $toasts as toast (toast.id)}
		<div
			class="data-[position=bottom-center]:origin-bottom data-[position=bottom-left]:origin-bottom-left data-[position=bottom-right]:origin-bottom-right data-[position=top-center]:origin-top data-[position=top-left]:origin-top-left data-[position=top-right]:origin-top-right"
			data-position={$_position}
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
