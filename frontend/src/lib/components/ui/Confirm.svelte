<script lang="ts">
	import { InfoIcon } from 'svelte-feather-icons'
	import { fly, fade } from 'svelte/transition'

	export let confirmText = 'Confirm'
	export let cancelText = 'Cancel'
	export let description = ''
	export let title = 'Confirm?'

	let showDialog = false

	let functionToCall = {
		func: null,
		args: null
	}

	function callFunction() {
		showDialog = true
		functionToCall['func'](...functionToCall['args'])
	}

	function confirm(func: any, ...args: any[]) {
		functionToCall = { func, args }
		showDialog = true
	}
</script>

<slot {confirm} />

{#if showDialog}
	<div
		class="fixed z-50 inset-0 overflow-y-auto"
		aria-labelledby="modal-title"
		role="dialog"
		aria-modal="true"
	>
		<div
			class="flex items-end justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0"
		>
			<div
				class="fixed inset-0 bg-zinc-800 cursor-pointer bg-opacity-75 transition-opacity"
				aria-hidden="true"
				on:click={() => (showDialog = false)}
				in:fade={{ duration: 300 }}
				out:fade={{ delay: 200, duration: 200 }}
			/>
			<!-- This element is to trick the browser into centering the modal contents. -->
			<span class="hidden sm:inline-block sm:align-middle sm:h-screen" aria-hidden="true"
				>&#8203;</span
			>
			<div
				class="inline-block align-bottom bg-white dark:bg-zinc-900 rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-lg sm:w-full"
				in:fly={{ y: -10, delay: 200, duration: 200 }}
				out:fly={{ y: -10, duration: 200 }}
			>
				<div class="px-4 pt-5 pb-4 sm:p-6 sm:pb-4">
					<div class="sm:flex sm:items-start">
						<div
							class="mx-auto flex-shrink-0 flex items-center justify-center h-12 w-12 rounded-full bg-blue-200 sm:mx-0 sm:h-10 sm:w-10"
						>
							<InfoIcon size="2x" class="text-blue-800" />
						</div>
						<div class="mt-3 text-center sm:mt-0 sm:ml-4 sm:text-left">
							<h3
								class="whitespace-pre-wrap text-lg leading-6 font-medium text-zinc-900 dark:text-white"
								id="modal-title"
							>
								{title}
							</h3>
							<div class="whitespace-pre-wrap mt-2 w-full text-sm text-zinc-500">{description}</div>
						</div>
					</div>
				</div>
				<div class="px-4 py-3 sm:px-6 flex flex-wrap sm:flex-row-reverse">
					<button
						type="button"
						on:click={callFunction}
						class="w-full inline-flex justify-center rounded-lg border border-transparent shadow-sm px-4 py-2 bg-red-600 text-base font-medium text-white hover:bg-red-700 focus:outline-none sm:ml-3 sm:w-auto sm:text-sm"
					>
						{confirmText}
					</button>
					<button
						type="button"
						on:click={() => (showDialog = false)}
						class="mt-3 w-full inline-flex justify-center rounded-lg border dark:text-white dark:hover:bg-zinc-700 dark:bg-zinc-900 border-zinc-300 dark:border-zinc-700 shadow-sm px-4 py-2 bg-white text-base font-medium text-zinc-700 hover:bg-zinc-50 focus:outline-none sm:mt-0 sm:ml-3 sm:w-auto sm:text-sm"
					>
						{cancelText}
					</button>
				</div>
			</div>
		</div>
	</div>
{/if}
