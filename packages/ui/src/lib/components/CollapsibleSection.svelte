<script lang="ts">
	import { MinusCircleIcon, PlusCircleIcon } from '../icons';
	import IconButton from './IconButton.svelte';

	interface Props {
		title: string;
		description: string;
	}

	let { title, description }: Props = $props();

	let open: boolean = $state(false);
</script>

<details
	class="rounded-lg bg-zinc-50 p-4 dark:bg-zinc-800 [&_summary::-webkit-details-marker]:hidden"
	{open}
>
	<summary
		class="flex cursor-pointer items-center justify-between gap-1.5 text-zinc-900 dark:text-white"
	>
		<h2 class="font-medium">
			{title}
		</h2>
		<IconButton
			src={open ? MinusCircleIcon : PlusCircleIcon}
			onclick={() => (open = !open)}
			class="h-6 w-6"
		/>
	</summary>
	{#if open}
		<p class="mt-4 text-sm leading-relaxed text-zinc-600 dark:text-zinc-300">
			{description}
		</p>
	{/if}
</details>
