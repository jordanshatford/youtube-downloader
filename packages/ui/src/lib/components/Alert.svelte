<script lang="ts">
	import type { HTMLAttributes } from 'svelte/elements';
	import { tv, type VariantProps } from 'tailwind-variants';
	import { Icon } from '../icons';
	import { toIcon } from '../utilities';

	const alert = tv({
		slots: {
			base: 'rounded border-s-4 p-4',
			icon: 'flex items-center gap-2',
			title: 'block font-medium',
			description: 'mt-2 text-sm'
		},
		variants: {
			variant: {
				error: {
					base: 'border-red-500 bg-red-50 dark:border-red-600 dark:bg-red-900',
					icon: 'text-red-800 dark:text-red-100',
					description: 'text-red-700 dark:text-red-200'
				},
				warning: {
					base: 'border-yellow-500 bg-yellow-50 dark:border-yellow-600 dark:bg-yellow-900',
					icon: 'text-yellow-800 dark:text-yellow-100',
					description: 'text-yellow-700 dark:text-yellow-200'
				},
				info: {
					base: 'border-blue-500 bg-blue-50 dark:border-blue-600 dark:bg-blue-900',
					icon: 'text-blue-800 dark:text-blue-100',
					description: 'text-blue-700 dark:text-blue-200'
				},
				success: {
					base: 'border-emerald-500 bg-emerald-50 dark:border-emerald-600 dark:bg-emerald-900',
					icon: 'text-emerald-800 dark:text-emerald-100',
					description: 'text-emerald-700 dark:text-emerald-200'
				}
			}
		},
		defaultVariants: {
			variant: 'info'
		}
	});

	interface $$Props extends HTMLAttributes<HTMLDivElement>, VariantProps<typeof alert> {
		title?: string;
		description?: string;
	}

	export let variant: $$Props['variant'] = 'info';
	export let title: $$Props['title'] = undefined;
	export let description: $$Props['title'] = undefined;

	const icon = toIcon(variant);

	const {
		base,
		icon: iconClass,
		title: titleClass,
		description: descriptionClass
	} = alert({ variant });
</script>

<div {...$$restProps} role="alert" class={base()}>
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
