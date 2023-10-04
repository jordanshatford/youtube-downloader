<script lang="ts" context="module">
	import { tv, type VariantProps } from 'tailwind-variants';

	const confirmClasses = tv({
		slots: {
			mainDivClass: 'px-4 pb-4 pt-5 sm:p-6 sm:pb-4',
			mainDivInnerClass: 'sm:flex sm:items-start',
			iconDivClass:
				'mx-auto flex h-12 w-12 flex-shrink-0 items-center justify-center rounded-full sm:mx-0 sm:h-10 sm:w-10',
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
	import { Button } from '../index';
	import { Icon } from '../icons';
	import { toIcon } from '../utilities';
	import { Modal } from '../index';

	export let variant: ConfirmVariants['variant'] = 'info';
	export let title: string = 'Confirm?';
	export let description: string = '';
	export let confirmText: string = 'Confirm';
	export let cancelText: string = 'Cancel';

	const icon = toIcon(variant);

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
	} = confirmClasses({
		variant
	});

	let showDialog = false;

	let onConfirmFunction: (() => void) | undefined = undefined;

	function callFunction() {
		showDialog = true;
		onConfirmFunction?.();
	}

	function confirm(f: () => void) {
		onConfirmFunction = f;
		showDialog = true;
	}
</script>

<slot {confirm} />

<Modal {...$$restProps} bind:show={showDialog}>
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
		<Button {variant} class={confirmButtonClass()} on:click={callFunction}>{confirmText}</Button>
		<Button variant="secondary" class={cancelButtonClass()} on:click={() => (showDialog = false)}
			>{cancelText}</Button
		>
	</div>
</Modal>
