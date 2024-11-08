<script lang="ts" module>
	import type { VariantProps } from 'tailwind-variants';
	import { tv } from 'tailwind-variants';

	const badgeClasses = tv({
		slots: {
			spanClass:
				'inline-flex items-center justify-center rounded-lg px-2.5 py-1 hover:cursor-default',
			iconWrapperClass: 'h-5',
			iconClass: '-ms-1 me-1.5 w-5',
			textClass: 'whitespace-nowrap text-sm h-5',
			buttonClass: '-me-1 ms-1.5 inline-block rounded-full p-0.5 w-4 h-4'
		},
		variants: {
			variant: {
				error: {
					spanClass: 'bg-red-100 text-red-700 dark:bg-red-700 dark:text-red-100',
					buttonClass:
						'bg-red-200 text-red-700 hover:bg-red-300 dark:bg-red-800 dark:text-red-100 dark:hover:bg-red-900'
				},
				warning: {
					spanClass: 'bg-yellow-100 text-yellow-700 dark:bg-yellow-700 dark:text-yellow-100',
					buttonClass:
						'bg-yellow-200 text-yellow-700 hover:bg-yellow-300 dark:bg-yellow-800 dark:text-yellow-100 dark:hover:bg-yellow-900'
				},
				info: {
					spanClass: 'bg-blue-100 text-blue-700 dark:bg-blue-700 dark:text-blue-100',
					buttonClass:
						'bg-blue-200 text-blue-700 hover:bg-blue-300 dark:bg-blue-800 dark:text-blue-100 dark:hover:bg-blue-900'
				},
				success: {
					spanClass: 'bg-emerald-100 text-emerald-700 dark:bg-emerald-700 dark:text-emerald-100',
					buttonClass:
						'bg-emerald-200 text-emerald-700 hover:bg-emerald-300 dark:bg-emerald-800 dark:text-emerald-100 dark:hover:bg-emerald-900'
				},
				default: {
					spanClass: 'bg-zinc-100 text-zinc-700 dark:bg-zinc-700 dark:text-zinc-100',
					buttonClass:
						'bg-zinc-200 text-zinc-700 hover:bg-zinc-300 dark:bg-zinc-800 dark:text-zinc-100 dark:hover:bg-zinc-900'
				}
			},
			loading: {
				true: {
					iconClass: 'animate-spin'
				}
			}
		},
		defaultVariants: {
			variant: 'default'
		}
	});

	export type BadgeVariants = VariantProps<typeof badgeClasses>;
</script>

<script lang="ts">
	import type { Snippet } from 'svelte';

	import type { IconSource } from '../icons';
	import { Icon, XMarkIcon } from '../icons';
	import { toIcon } from '../utilities';

	interface Props {
		class?: string;
		variant?: BadgeVariants['variant'];
		closable?: boolean;
		onclose?: () => void;
		icon?: boolean | IconSource;
		loading?: boolean;
		children?: Snippet;
	}

	let {
		class: className = '',
		variant = 'default',
		closable = false,
		onclose = undefined,
		icon = false,
		loading = false,
		children
	}: Props = $props();

	let _icon: IconSource | undefined = $state(undefined);
	// User specified icon
	if (typeof icon === 'object') {
		_icon = icon;
	} else if (icon) {
		_icon = toIcon(variant, { loading });
	}

	const { spanClass, iconWrapperClass, iconClass, textClass, buttonClass } = badgeClasses({
		variant,
		loading
	});
</script>

<span class={spanClass({ class: className })}>
	<span class={iconWrapperClass()}>
		{#if _icon}
			<Icon src={_icon} theme="solid" class={iconClass()} />
		{/if}
	</span>
	<p class={textClass()}>{@render children?.()}</p>
	{#if closable}
		<button class={buttonClass()} onclick={() => onclose?.()}>
			<span class="sr-only">Remove badge</span>
			<Icon src={XMarkIcon} theme="solid" />
		</button>
	{/if}
</span>
