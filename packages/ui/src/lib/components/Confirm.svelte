<script lang="ts">
	import { fly, fade } from 'svelte/transition';
	import type { Variant } from '../types';
	import { variantMapping } from '../utilities';
	import { Icon } from '../icons';

	export let confirmText = 'Confirm';
	export let cancelText = 'Cancel';
	export let description = '';
	export let title = 'Confirm?';
	export let variant: Variant = 'default';

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
		<div
			class="flex min-h-screen items-end justify-center px-4 pb-20 pt-4 text-center sm:block sm:p-0"
		>
			<div
				class="fixed inset-0 cursor-pointer bg-zinc-800 bg-opacity-75 transition-opacity"
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
				class="inline-block transform overflow-hidden rounded-lg bg-white text-left align-bottom shadow-xl transition-all dark:bg-zinc-900 sm:my-8 sm:w-full sm:max-w-lg sm:align-middle"
				in:fly={{ y: -10, delay: 200, duration: 200 }}
				out:fly={{ y: -10, duration: 200 }}
			>
				<div class="px-4 pb-4 pt-5 sm:p-6 sm:pb-4">
					<div class="sm:flex sm:items-start">
						<div
							class="mx-auto flex h-12 w-12 flex-shrink-0 items-center justify-center rounded-full bg-blue-200 sm:mx-0 sm:h-10 sm:w-10 {variantMapping[
								variant
							].class}"
						>
							<Icon src={variantMapping[variant].icon} class="h-8 w-8" />
						</div>
						<div class="mt-3 text-center sm:ml-4 sm:mt-0 sm:text-left">
							<h3
								class="whitespace-pre-wrap text-lg font-medium leading-6 text-zinc-900 dark:text-white"
								id="modal-title"
							>
								{title}
							</h3>
							<div class="mt-2 w-full whitespace-pre-wrap text-sm text-zinc-500">{description}</div>
						</div>
					</div>
				</div>
				<div class="flex flex-wrap px-4 py-3 sm:flex-row-reverse sm:px-6">
					<button
						type="button"
						on:click={callFunction}
						class="inline-flex w-full justify-center rounded-lg border border-transparent bg-red-600 px-4 py-2 text-base font-medium text-white shadow-sm hover:bg-red-700 focus:outline-none sm:ml-3 sm:w-auto sm:text-sm"
					>
						{confirmText}
					</button>
					<button
						type="button"
						on:click={() => (showDialog = false)}
						class="mt-3 inline-flex w-full justify-center rounded-lg border border-zinc-300 bg-white px-4 py-2 text-base font-medium text-zinc-700 shadow-sm hover:bg-zinc-50 focus:outline-none dark:border-zinc-700 dark:bg-zinc-900 dark:text-white dark:hover:bg-zinc-700 sm:ml-3 sm:mt-0 sm:w-auto sm:text-sm"
					>
						{cancelText}
					</button>
				</div>
			</div>
		</div>
	</div>
{/if}
