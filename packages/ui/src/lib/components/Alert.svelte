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
					divClass: 'border-red-500 bg-red-50 dark:border-red-600 dark:bg-red-900',
					iconClass: 'text-red-800 dark:text-red-100',
					descriptionClass: 'text-red-700 dark:text-red-200'
				},
				warning: {
					divClass: 'border-yellow-500 bg-yellow-50 dark:border-yellow-600 dark:bg-yellow-900',
					iconClass: 'text-yellow-800 dark:text-yellow-100',
					descriptionClass: 'text-yellow-700 dark:text-yellow-200'
				},
				info: {
					divClass: 'border-blue-500 bg-blue-50 dark:border-blue-600 dark:bg-blue-900',
					iconClass: 'text-blue-800 dark:text-blue-100',
					descriptionClass: 'text-blue-700 dark:text-blue-200'
				},
				success: {
					divClass: 'border-emerald-500 bg-emerald-50 dark:border-emerald-600 dark:bg-emerald-900',
					iconClass: 'text-emerald-800 dark:text-emerald-100',
					descriptionClass: 'text-emerald-700 dark:text-emerald-200'
				}
			}
		},
		defaultVariants: {
			variant: 'info'
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

	export let variant: $$Props['variant'] = 'info';
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
