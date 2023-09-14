<script lang="ts">
	import { MinusCircleIcon, PlusCircleIcon } from '../icons';
	import IconButton from './IconButton.svelte';

	export let question: string;
	export let answer: string;

	let open: boolean = false;
</script>

<details
	class="rounded-lg bg-zinc-50 p-4 dark:bg-zinc-800 [&_summary::-webkit-details-marker]:hidden"
	{open}
>
	<summary
		class="flex cursor-pointer items-center justify-between gap-1.5 text-zinc-900 dark:text-white"
	>
		<h2 class="font-medium">
			{question}
		</h2>
		<IconButton
			src={open ? MinusCircleIcon : PlusCircleIcon}
			on:click={() => (open = !open)}
			class="h-10 w-10"
		/>
	</summary>
	{#if open}
		<p class="mt-4 text-sm leading-relaxed text-zinc-600 dark:text-zinc-300">
			{answer}
		</p>
	{/if}
</details>
