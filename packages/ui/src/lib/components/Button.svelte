<script lang="ts" module>
	import type { VariantProps } from 'tailwind-variants';
	import { tv } from 'tailwind-variants';

	const buttonClasses = tv({
		base: 'rounded-lg border border-transparent px-4 py-2 text-center text-base font-medium text-white shadow-xs focus:outline-hidden disabled:cursor-not-allowed disabled:opacity-75 hover:cursor-pointer',
		variants: {
			variant: {
				error: 'bg-red-700 hover:bg-red-600 disabled:hover:bg-red-700',
				warning: 'bg-yellow-700 hover:bg-yellow-600 disabled:hover:bg-yellow-700',
				info: 'bg-blue-700 hover:bg-blue-600 disabled:hover:bg-blue-700',
				success: 'bg-emerald-700 hover:bg-emerald-600 disabled:hover:bg-emerald-700',
				secondary:
					'border-zinc-300 bg-white text-zinc-700 hover:bg-zinc-50 dark:border-zinc-700 dark:bg-zinc-900 dark:text-white dark:hover:bg-zinc-700'
			}
		},
		defaultVariants: {
			variant: 'info'
		}
	});

	export type ButtonVariants = VariantProps<typeof buttonClasses>;
</script>

<script lang="ts">
	import type { Snippet } from 'svelte';
	import type { HTMLButtonAttributes } from 'svelte/elements';

	interface Props extends HTMLButtonAttributes {
		variant?: ButtonVariants['variant'];
		href?: string | undefined;
		children?: Snippet;
	}

	let { variant = 'info', href = undefined, children, class: className, ...rest }: Props = $props();

	const buttonClass = buttonClasses({ variant, class: String(className) });
</script>

{#if href}
	<a {href} class={buttonClass}>
		{@render children?.()}
	</a>
{:else}
	<button {...rest} type="button" class={buttonClass}>
		{@render children?.()}
	</button>
{/if}
