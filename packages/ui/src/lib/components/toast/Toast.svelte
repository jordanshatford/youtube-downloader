<script lang="ts" context="module">
	import { tv, type VariantProps } from 'tailwind-variants';

	const toastClasses = tv({
		slots: {
			outerDivClass: 'pointer-events-auto relative flex space-y-5',
			outerContentDivClass:
				'border-secondary-50 relative mx-auto min-w-[300px] max-w-[400px] rounded-xl border bg-white p-3 text-sm shadow-lg dark:border-zinc-700 dark:bg-zinc-900',
			contentDivClass: 'flex space-x-4',
			closeIconClass:
				'absolute right-3 top-2 ml-auto h-4 w-4 text-zinc-500 hover:text-zinc-900 dark:text-zinc-100 dark:hover:text-zinc-500',
			iconDivClass: 'flex h-10 w-10 items-center justify-center rounded-full',
			iconClass: 'h-6 w-6',
			textDivClass: 'flex-1',
			titleClass: 'pr-6 font-medium text-zinc-900 dark:text-zinc-100',
			descriptionClass: 'mt-1 text-zinc-500 dark:text-zinc-300'
		},
		variants: {
			variant: {
				error: {
					iconDivClass: 'bg-red-100 text-red-700 dark:bg-red-700 dark:text-red-100'
				},
				warning: {
					iconDivClass: 'bg-yellow-100 text-yellow-700 dark:bg-yellow-700 dark:text-yellow-100'
				},
				info: {
					iconDivClass: 'bg-blue-100 text-blue-700 dark:bg-blue-700 dark:text-blue-100'
				},
				success: {
					iconDivClass: 'bg-emerald-100 text-emerald-700 dark:bg-emerald-700 dark:text-emerald-100'
				},
				promise: {
					iconDivClass: 'bg-blue-100 text-blue-700 dark:bg-blue-700 dark:text-blue-100'
				}
			}
		},
		defaultVariants: {
			variant: 'info'
		},
		compoundSlots: [
			{
				slots: ['iconClass'],
				variant: 'promise',
				class: 'animate-spin'
			}
		]
	});

	export type ToastVariants = VariantProps<typeof toastClasses>;
</script>

<script lang="ts">
	import { toast as _toast } from './stores';
	import type { ToastComponent } from './types';
	import { XMarkIcon, Icon } from '../../icons';
	import { toIcon } from '../../utilities';
	import IconButton from '../IconButton.svelte';

	export let toast: ToastComponent;

	$: icon = toIcon(toast.variant);

	const {
		outerDivClass,
		outerContentDivClass,
		contentDivClass,
		closeIconClass,
		iconDivClass,
		iconClass,
		textDivClass,
		titleClass,
		descriptionClass
	} = toastClasses({
		variant: toast.variant
	});
</script>

<div id="yd-toast-{toast.id}" aria-live="polite" role="status" class={outerDivClass()}>
	<div class={outerContentDivClass()}>
		{#if toast.closable && toast.variant !== 'promise'}
			<IconButton
				src={XMarkIcon}
				class={closeIconClass()}
				on:click={() => _toast.remove(toast.id)}
			/>
		{/if}
		<div class={contentDivClass()}>
			{#if icon}
				<div class={iconDivClass({ variant: toast.variant })}>
					<Icon src={icon} theme="solid" class={iconClass({ variant: toast.variant })} />
				</div>
			{/if}
			<div class={textDivClass()}>
				<h4 class={titleClass()}>{toast.title}</h4>
				<div class={descriptionClass()}>
					{toast.description}
				</div>
			</div>
		</div>
	</div>
</div>
