<script lang="ts">
	import type { HTMLInputAttributes } from 'svelte/elements';

	interface Props extends HTMLInputAttributes {
		label: string;
		helpText?: string;
		checked: boolean | undefined;
	}

	let { id, label, helpText = '', checked = $bindable(), ...rest }: Props = $props();
</script>

<div class="flex justify-between space-x-2 py-3">
	<label for={id}>
		<div class="dark:text-white">{label}</div>
		<p class="text-sm text-zinc-500">{helpText}</p>
	</label>
	<div class="flex h-8 items-center">
		<label for={id} class="relative h-6 w-10 cursor-pointer">
			<input {...rest} type="checkbox" {id} bind:checked class="peer sr-only" />
			<span
				class="absolute inset-0 rounded-full bg-zinc-300 transition peer-checked:bg-blue-500 peer-disabled:cursor-not-allowed peer-disabled:opacity-50 dark:bg-zinc-600"
			></span>
			<span
				class="absolute inset-y-0 start-0 m-1 h-4 w-4 rounded-full bg-white transition-all peer-checked:start-4 peer-disabled:cursor-not-allowed peer-disabled:opacity-50"
			></span>
		</label>
	</div>
</div>
