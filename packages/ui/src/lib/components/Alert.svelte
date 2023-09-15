<script lang="ts" context="module">
	import { tv, type VariantProps } from 'tailwind-variants';

	const alert = tv({
		slots: {
			divClass: 'rounded border-s-4 p-4',
			iconClass: 'flex items-center gap-2',
			titleClass: 'block font-medium',
			descriptionClass: 'mt-2 text-sm'
		},
		variants: {
			variant: {
				error: {
					divClass: 'border-red-500 bg-red-100 dark:border-red-600 dark:bg-red-800',
					iconClass: 'text-red-700 dark:text-red-100',
					descriptionClass: 'text-red-700 dark:text-red-200'
				},
				warning: {
					divClass: 'border-yellow-500 bg-yellow-100 dark:border-yellow-600 dark:bg-yellow-800',
					iconClass: 'text-yellow-700 dark:text-yellow-100',
					descriptionClass: 'text-yellow-700 dark:text-yellow-200'
				},
				info: {
					divClass: 'border-blue-500 bg-blue-100 dark:border-blue-600 dark:bg-blue-800',
					iconClass: 'text-blue-700 dark:text-blue-100',
					descriptionClass: 'text-blue-700 dark:text-blue-200'
				},
				success: {
					divClass: 'border-emerald-500 bg-emerald-100 dark:border-emerald-600 dark:bg-emerald-800',
					iconClass: 'text-emerald-700 dark:text-emerald-100',
					descriptionClass: 'text-emerald-700 dark:text-emerald-200'
				},
				default: {
					divClass: 'border-zinc-500 bg-zinc-100 dark:border-zinc-400 dark:bg-zinc-700',
					iconClass: 'text-zinc-700 dark:text-zinc-100',
					descriptionClass: 'text-zinc-700 dark:text-zinc-100'
				}
			}
		},
		defaultVariants: {
			variant: 'default'
		}
	});

	export type AlertVariants = VariantProps<typeof alert>;
</script>

<script lang="ts">
	import type { HTMLAttributes } from 'svelte/elements';
	import { Icon } from '../icons';
	import { toIcon } from '../utilities';

	interface $$Props extends HTMLAttributes<HTMLDivElement>, AlertVariants {
		title?: string;
		description?: string;
	}

	export let variant: $$Props['variant'] = 'default';
	export let title: $$Props['title'] = undefined;
	export let description: $$Props['title'] = undefined;

	const icon = toIcon(variant);

	const { divClass, iconClass, titleClass, descriptionClass } = alert({ variant });
</script>

<div {...$$restProps} role="alert" class={divClass({ class: $$props.class })}>
	<div class={iconClass()}>
		{#if icon}
			<Icon src={icon} theme="solid" class="h-5 w-5" />
		{/if}
		<strong class={titleClass()}>
			<slot>
				{#if title}
					{title}
				{/if}
			</slot>
		</strong>
	</div>
	<p class={descriptionClass()}>
		<slot name="description">
			{#if description}
				{description}
			{/if}
		</slot>
	</p>
</div>
