<script lang="ts" module>
	import type { VariantProps } from 'tailwind-variants';
	import { tv } from 'tailwind-variants';

	const confirmClasses = tv({
		slots: {
			mainDivClass: 'px-4 pb-4 pt-5 sm:p-6 sm:pb-4',
			mainDivInnerClass: 'sm:flex sm:items-start',
			iconDivClass:
				'mx-auto flex h-12 w-12 shrink-0 items-center justify-center rounded-full sm:mx-0 sm:h-10 sm:w-10',
			iconClass: 'h-8 w-8',
			textDivClass: 'mt-3 text-center sm:ml-4 sm:mt-0 sm:text-left',
			titleClass: 'whitespace-pre-wrap text-lg font-medium leading-6 text-zinc-900 dark:text-white',
			descriptionClass: 'mt-2 w-full whitespace-pre-wrap text-sm text-zinc-500',
			footerDivClass: 'flex flex-wrap px-4 py-3 sm:flex-row-reverse sm:px-6',
			confirmButtonClass: 'inline-flex w-full justify-center sm:ml-3 sm:w-auto sm:text-sm',
			cancelButtonClass:
				'mt-3 inline-flex w-full justify-center sm:ml-3 sm:mt-0 sm:w-auto sm:text-sm'
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
				}
			}
		},
		defaultVariants: {
			variant: 'info'
		}
	});

	export type ConfirmVariants = VariantProps<typeof confirmClasses>;
</script>

<script lang="ts">
	import type { Snippet } from 'svelte';

	import { Icon } from '../icons';
	import { Button, Modal } from '../index';
	import { toIcon } from '../utilities';

	interface Props {
		variant?: ConfirmVariants['variant'];
		title?: string;
		description?: string;
		confirmText?: string;
		cancelText?: string;
		children?: Snippet<[{ confirm: (f: () => void) => void }]>;
	}

	let {
		variant = 'info',
		title = 'Confirm?',
		description = '',
		confirmText = 'Confirm',
		cancelText = 'Cancel',
		children
	}: Props = $props();

	const icon = $derived(toIcon(variant));

	const {
		mainDivClass,
		mainDivInnerClass,
		iconDivClass,
		iconClass,
		textDivClass,
		titleClass,
		descriptionClass,
		footerDivClass,
		confirmButtonClass,
		cancelButtonClass
	} = $derived(
		confirmClasses({
			variant
		})
	);

	let showDialog = $state(false);

	let onConfirmFunction: (() => void) | undefined = undefined;

	function callFunction() {
		showDialog = true;
		onConfirmFunction?.();
		showDialog = false;
	}

	function confirm(f: () => void) {
		onConfirmFunction = f;
		showDialog = true;
	}
</script>

{@render children?.({ confirm })}

<Modal bind:show={showDialog}>
	<div class={mainDivClass()}>
		<div class={mainDivInnerClass()}>
			{#if icon}
				<div class={iconDivClass()}>
					<Icon src={icon} theme="solid" class={iconClass()} />
				</div>
			{/if}
			<div class={textDivClass()}>
				<h3 class={titleClass()} id="modal-title">
					{title}
				</h3>
				<div class={descriptionClass()}>{description}</div>
			</div>
		</div>
	</div>
	<div class={footerDivClass()}>
		<Button {variant} class={confirmButtonClass()} onclick={callFunction}>{confirmText}</Button>
		<Button variant="secondary" class={cancelButtonClass()} onclick={() => (showDialog = false)}
			>{cancelText}</Button
		>
	</div>
</Modal>
