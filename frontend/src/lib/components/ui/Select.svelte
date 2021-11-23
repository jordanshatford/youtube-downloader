<script lang="ts">
	export let title: string
	export let value: number | string
	export let options: { value: number | string; text: string }[]
	export let disabled = false
</script>

<div>
	<p class="p-2 dark:text-white">{title}</p>
	<select
		{disabled}
		on:change
		bind:value
		class="w-full p-2 text-gray-600 dark:text-gray-200 rounded-md border-2 border-gray-200 dark:border-gray-600 outline-none dark:bg-gray-800 dark:disabled:bg-gray-600"
	>
		{#each options as option}
			<option value={option.value} class="py-1">{option.text}</option>
		{/each}
	</select>
</div>
