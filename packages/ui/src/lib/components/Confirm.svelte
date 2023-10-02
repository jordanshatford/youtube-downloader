<script lang="ts" context="module">
	import { tv, type VariantProps } from 'tailwind-variants';

	const confirmClasses = tv({
		slots: {
			outerDivClass: 'fixed inset-0 z-50 overflow-y-auto',
			backgroundOuterDivClass:
				'flex min-h-screen items-end justify-center px-4 pb-20 pt-4 text-center sm:block sm:p-0',
			backgroundTransitionDivClass:
				'fixed inset-0 cursor-pointer bg-zinc-800 bg-opacity-75 transition-opacity',
			trickCenteringSpanClass: 'hidden sm:inline-block sm:h-screen sm:align-middle',
			contentDivClass:
				'inline-block transform overflow-hidden rounded-lg bg-white text-left align-bottom shadow-xl transition-all dark:bg-zinc-900 sm:my-8 sm:w-full sm:max-w-lg sm:align-middle',
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
	import { fly, fade } from 'svelte/transition';
	import { Button } from '../index';
	import { Icon } from '../icons';
	import { toIcon } from '../utilities';

	let className: string = '';
	export { className as class };

	export let variant: ConfirmVariants['variant'] = 'info';
	export let title: string = 'Confirm?';
	export let description: string = '';
	export let confirmText: string = 'Confirm';
	export let cancelText: string = 'Cancel';

	const icon = toIcon(variant);

	const {
		outerDivClass,
		backgroundOuterDivClass,
		backgroundTransitionDivClass,
		trickCenteringSpanClass,
		contentDivClass,
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

{#if showDialog}
	<div class={outerDivClass()} aria-labelledby="modal-title" role="dialog" aria-modal="true">
		<div class={backgroundOuterDivClass()}>
			<div
				class={backgroundTransitionDivClass()}
				aria-hidden="true"
				on:click={() => (showDialog = false)}
				in:fade={{ duration: 300 }}
				out:fade={{ delay: 200, duration: 200 }}
			/>
			<!-- This element is to trick the browser into centering the modal contents. -->
			<span class={trickCenteringSpanClass()} aria-hidden="true">&#8203;</span>
			<div
				{...$$restProps}
				class={contentDivClass({ class: className })}
				in:fly={{ y: -10, delay: 200, duration: 200 }}
				out:fly={{ y: -10, duration: 200 }}
			>
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
					<Button {variant} class={confirmButtonClass()} on:click={callFunction}
						>{confirmText}</Button
					>
					<Button
						variant="secondary"
						class={cancelButtonClass()}
						on:click={() => (showDialog = false)}>{cancelText}</Button
					>
				</div>
			</div>
		</div>
	</div>
{/if}
