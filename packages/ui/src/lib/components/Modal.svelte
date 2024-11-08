<script lang="ts">
	import type { Snippet } from 'svelte';
	import type { HTMLHtmlAttributes } from 'svelte/elements';
	import { fade, fly } from 'svelte/transition';
	import { tv } from 'tailwind-variants';

	const modalClasses = tv({
		slots: {
			outerDivClass: 'fixed inset-0 z-50 overflow-y-auto',
			backgroundOuterDivClass:
				'flex min-h-screen items-end justify-center px-4 pb-20 pt-4 text-center sm:block sm:p-0',
			backgroundTransitionDivClass:
				'fixed inset-0 cursor-pointer bg-zinc-800 bg-opacity-75 transition-opacity',
			trickCenteringSpanClass: 'hidden sm:inline-block sm:h-screen sm:align-middle',
			contentDivClass:
				'inline-block transform overflow-hidden rounded-lg bg-white text-left align-bottom shadow-xl transition-all dark:bg-zinc-900 sm:my-8 sm:w-full sm:max-w-lg sm:align-middle'
		}
	});

	interface Props extends HTMLHtmlAttributes {
		show?: boolean;
		children?: Snippet;
	}

	let { show = $bindable(false), class: className, children }: Props = $props();

	const {
		outerDivClass,
		backgroundOuterDivClass,
		backgroundTransitionDivClass,
		trickCenteringSpanClass,
		contentDivClass
	} = modalClasses();
</script>

{#if show}
	<div class={outerDivClass()} aria-labelledby="modal-title" role="dialog" aria-modal="true">
		<div class={backgroundOuterDivClass()}>
			<div
				class={backgroundTransitionDivClass()}
				aria-hidden="true"
				onclick={() => (show = false)}
				in:fade={{ duration: 300 }}
				out:fade={{ delay: 200, duration: 200 }}
			></div>
			<!-- This element is to trick the browser into centering the modal contents. -->
			<span class={trickCenteringSpanClass()} aria-hidden="true">&#8203;</span>
			<div
				class={contentDivClass({ class: className })}
				in:fly={{ y: -10, delay: 200, duration: 200 }}
				out:fly={{ y: -10, duration: 200 }}
			>
				{@render children?.()}
			</div>
		</div>
	</div>
{/if}
