<script lang="ts">
	import type { HTMLSelectAttributes } from 'svelte/elements';

	interface SelectOption {
		value: number | string | boolean;
		text: string;
	}

	interface Props extends HTMLSelectAttributes {
		label: string;
		helpText?: string | undefined;
		value: number | string | boolean | undefined;
		options?: SelectOption[];
		groups?: { text: string; disabled?: boolean; options: SelectOption[] }[];
	}

	let {
		id,
		label,
		helpText = undefined,
		value = $bindable(),
		options = [],
		groups = [],
		...rest
	}: Props = $props();
</script>

<div>
	<label for={id} class="my-1 block dark:text-white">{label}</label>
	<select
		{...rest}
		{id}
		bind:value
		class="w-full rounded-lg border-2 border-zinc-200 p-2 text-zinc-600 outline-none focus:border-blue-600 focus:ring-transparent disabled:cursor-not-allowed disabled:bg-zinc-200 dark:border-zinc-600 dark:bg-zinc-800 dark:text-zinc-200 dark:focus:border-blue-600 dark:disabled:bg-zinc-600"
	>
		{#if groups.length > 0}
			{#each groups as group}
				<optgroup label={group.text} disabled={group.disabled}>
					{#each group.options as option}
						<option value={option.value}>{option.text}</option>
					{/each}
				</optgroup>
			{/each}
		{:else}
			{#each options as option}
				<option value={option.value}>{option.text}</option>
			{/each}
		{/if}
	</select>
	{#if helpText}
		<p class="mt-1 text-sm text-zinc-500">{helpText}</p>
	{/if}
</div>
