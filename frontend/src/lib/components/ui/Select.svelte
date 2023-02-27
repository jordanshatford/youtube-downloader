<script lang="ts">
	export let title: string;
	export let value: number | string;
	export let options: { value: number | string; text: string }[];
	export let disabled = false;
</script>

<div>
	<p class="p-2 dark:text-white">{title}</p>
	<select
		{disabled}
		on:change
		bind:value
		class="w-full p-2 text-zinc-600 dark:text-zinc-200 rounded-lg border-2 border-zinc-200 dark:border-zinc-600 outline-none dark:bg-zinc-800 dark:disabled:bg-zinc-600"
	>
		{#each options as option}
			<option value={option.value} class="py-1">{option.text}</option>
		{/each}
	</select>
</div>
