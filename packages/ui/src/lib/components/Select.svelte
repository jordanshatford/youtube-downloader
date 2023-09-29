<script lang="ts">
	export let title: string;
	export let value: number | string | boolean | undefined;
	export let options: { value: number | string | boolean; text: string }[];
	export let disabled = false;
</script>

<div>
	<p class="p-2 dark:text-white">{title}</p>
	<select
		{...$$restProps}
		{disabled}
		on:change
		bind:value
		class="w-full rounded-lg border-2 border-zinc-200 p-2 text-zinc-600 outline-none focus:border-indigo-600 focus:ring-transparent dark:border-zinc-600 dark:bg-zinc-800 dark:text-zinc-200 dark:disabled:bg-zinc-600"
	>
		{#each options as option}
			<option value={option.value} class="py-1">{option.text}</option>
		{/each}
	</select>
</div>
