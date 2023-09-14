<script lang="ts" context="module">
	import { tv, type VariantProps } from 'tailwind-variants';

	const confirmClasses = tv({
		slots: {
			backgroundOuterDivClass:
				'flex min-h-screen items-end justify-center px-4 pb-20 pt-4 text-center sm:block sm:p-0',
			backgroundTransitionDivClass:
				'fixed inset-0 cursor-pointer bg-zinc-800 bg-opacity-75 transition-opacity',
			contentDivClass:
				'inline-block transform overflow-hidden rounded-lg bg-white text-left align-bottom shadow-xl transition-all dark:bg-zinc-900 sm:my-8 sm:w-full sm:max-w-lg sm:align-middle',
			mainDivClass: 'px-4 pb-4 pt-5 sm:p-6 sm:pb-4',
			iconDivClass:
				'mx-auto flex h-12 w-12 flex-shrink-0 items-center justify-center rounded-full sm:mx-0 sm:h-10 sm:w-10',
			titleClass: 'whitespace-pre-wrap text-lg font-medium leading-6 text-zinc-900 dark:text-white',
			descriptionClass: 'mt-2 w-full whitespace-pre-wrap text-sm text-zinc-500',
			footerDivClass: 'flex flex-wrap px-4 py-3 sm:flex-row-reverse sm:px-6',
			confirmButtonClass:
				'inline-flex w-full justify-center rounded-lg border border-transparent px-4 py-2 text-base font-medium text-white shadow-sm focus:outline-none sm:ml-3 sm:w-auto sm:text-sm',
			cancelButtonClass:
				'mt-3 inline-flex w-full justify-center rounded-lg border border-zinc-300 bg-white px-4 py-2 text-base font-medium text-zinc-700 shadow-sm hover:bg-zinc-50 focus:outline-none dark:border-zinc-700 dark:bg-zinc-900 dark:text-white dark:hover:bg-zinc-700 sm:ml-3 sm:mt-0 sm:w-auto sm:text-sm'
		},
		variants: {
			variant: {
				error: {
					iconDivClass: 'text-red-500 bg-red-100',
					confirmButtonClass: 'bg-red-600 hover:bg-red-700'
				},
				warning: {
					iconDivClass: 'text-yellow-800 bg-yellow-200',
					confirmButtonClass: 'bg-yellow-600 hover:bg-yellow-700'
				},
				info: {
					iconDivClass: 'text-blue-800 bg-blue-200',
					confirmButtonClass: 'bg-blue-600 hover:bg-blue-700'
				},
				success: {
					iconDivClass: 'text-emerald-800 bg-emerald-200',
					confirmButtonClass: 'bg-emerald-600 hover:bg-emerald-700'
				},
				default: {
					iconDivClass: 'text-zinc-800 bg-zinc-200',
					confirmButtonClass:
						'border-zinc-300 bg-white text-zinc-700 hover:bg-zinc-50 dark:border-zinc-700 dark:bg-zinc-900 dark:text-white dark:hover:bg-zinc-700'
				}
			}
		},
		defaultVariants: {
			variant: 'default'
		}
	});

	export type ConfirmVariants = VariantProps<typeof confirmClasses>;
</script>

<script lang="ts">
	import type { HTMLAttributes } from 'svelte/elements';
	import { fly, fade } from 'svelte/transition';
	import { Icon } from '../icons';
	import { toIcon } from '../utilities';

	interface $$Props extends HTMLAttributes<HTMLDivElement>, ConfirmVariants {
		title: string;
		description: string;
		confirmText: string;
		cancelText: string;
	}

	export let variant: $$Props['variant'] = 'info';
	export let title: $$Props['title'] = 'Confirm?';
	export let description: $$Props['description'] = '';
	export let confirmText: $$Props['confirmText'] = 'Confirm';
	export let cancelText: $$Props['cancelText'] = 'Cancel';

	const icon = toIcon(variant);

	const {
		backgroundOuterDivClass,
		backgroundTransitionDivClass,
		contentDivClass,
		mainDivClass,
		iconDivClass,
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
	<div
		class="fixed inset-0 z-50 overflow-y-auto"
		aria-labelledby="modal-title"
		role="dialog"
		aria-modal="true"
	>
		<div class={backgroundOuterDivClass()}>
			<div
				class={backgroundTransitionDivClass()}
				aria-hidden="true"
				on:click={() => (showDialog = false)}
				in:fade={{ duration: 300 }}
				out:fade={{ delay: 200, duration: 200 }}
			/>
			<!-- This element is to trick the browser into centering the modal contents. -->
			<span class="hidden sm:inline-block sm:h-screen sm:align-middle" aria-hidden="true"
				>&#8203;</span
			>
			<div
				{...$$restProps}
				class={contentDivClass({ class: $$props.class })}
				in:fly={{ y: -10, delay: 200, duration: 200 }}
				out:fly={{ y: -10, duration: 200 }}
			>
				<div class={mainDivClass()}>
					<div class="sm:flex sm:items-start">
						{#if icon}
							<div class={iconDivClass()}>
								<Icon src={icon} theme="outline" class="h-8 w-8" />
							</div>
						{/if}
						<div class="mt-3 text-center sm:ml-4 sm:mt-0 sm:text-left">
							<h3 class={titleClass()} id="modal-title">
								{title}
							</h3>
							<div class={descriptionClass()}>{description}</div>
						</div>
					</div>
				</div>
				<div class={footerDivClass()}>
					<button type="button" on:click={callFunction} class={confirmButtonClass()}>
						{confirmText}
					</button>
					<button type="button" on:click={() => (showDialog = false)} class={cancelButtonClass()}>
						{cancelText}
					</button>
				</div>
			</div>
		</div>
	</div>
{/if}
