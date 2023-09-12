<script lang="ts">
	import { createEventDispatcher } from 'svelte';
	import type { HTMLAttributes } from 'svelte/elements';
	import { tv, type VariantProps } from 'tailwind-variants';
	import { Icon, XMarkIcon, type IconSource } from '../icons';
	import { toIcon } from '../utilities';

	const badge = tv({
		slots: {
			base: 'inline-flex items-center justify-center rounded-lg px-2.5 py-1',
			content: 'whitespace-nowrap text-sm h-5',
			closeButton: '-me-1 ms-1.5 inline-block rounded-full p-0.5 w-4 h-4'
		},
		variants: {
			variant: {
				error: {
					base: 'bg-red-100 text-red-700 dark:bg-red-700 dark:text-red-100',
					closeButton:
						'bg-red-200 text-red-700 hover:bg-red-300 dark:bg-red-800 dark:text-red-100 dark:hover:bg-red-900'
				},
				warning: {
					base: 'bg-yellow-100 text-yellow-700 dark:bg-yellow-700 dark:text-yellow-100',
					closeButton:
						'bg-yellow-200 text-yellow-700 hover:bg-yellow-300 dark:bg-yellow-800 dark:text-yellow-100 dark:hover:bg-yellow-900'
				},
				info: {
					base: 'bg-blue-100 text-blue-700 dark:bg-blue-700 dark:text-blue-100',
					closeButton:
						'bg-blue-200 text-blue-700 hover:bg-blue-300 dark:bg-blue-800 dark:text-blue-100 dark:hover:bg-blue-900'
				},
				success: {
					base: 'bg-emerald-100 text-emerald-700 dark:bg-emerald-700 dark:text-emerald-100',
					closeButton:
						'bg-emerald-200 text-emerald-700 hover:bg-emerald-300 dark:bg-emerald-800 dark:text-emerald-100 dark:hover:bg-emerald-900'
				},
				default: {
					base: 'bg-zinc-100 text-zinc-700 dark:bg-zinc-700 dark:text-zinc-100',
					closeButton:
						'bg-zinc-200 text-zinc-700 hover:bg-zinc-300 dark:bg-zinc-800 dark:text-zinc-100 dark:hover:bg-zinc-900'
				}
			}
		},
		defaultVariants: {
			variant: 'default'
		}
	});

	const dispatch = createEventDispatcher<{
		close: undefined;
	}>();

	interface $$Props extends HTMLAttributes<HTMLSpanElement>, VariantProps<typeof badge> {
		closable?: boolean;
		showIcon?: boolean;
		icon?: IconSource;
	}

	export let variant: $$Props['variant'] = 'default';
	export let closable: $$Props['closable'] = false;
	export let showIcon: $$Props['showIcon'] = false;
	export let icon: $$Props['icon'] = toIcon(variant);

	const { base, content, closeButton } = badge({ variant });
</script>

<span {...$$restProps} class={base()}>
	<span class="h-5">
		{#if showIcon && icon}
			<Icon src={icon} theme="solid" class="-ms-1 me-1.5 w-5" />
		{/if}
	</span>
	<p class={content()}><slot /></p>
	{#if closable}
		<button class={closeButton()} on:click={() => dispatch('close')}>
			<span class="sr-only">Remove badge</span>
			<Icon src={XMarkIcon} theme="solid" />
		</button>
	{/if}
</span>
