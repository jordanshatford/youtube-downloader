<script lang="ts">
	export let title: string;
	export let value: number | string | boolean | undefined;
	export let options: { value: number | string | boolean; text: string }[] = [];
	export let groups: { text: string; disabled?: boolean; options: typeof options }[] = [];
	export let disabled = false;
</script>

<div>
	<p class="p-2 dark:text-white">{title}</p>
	<select
		{...$$restProps}
		{disabled}
		bind:value
		on:change
		class="w-full rounded-lg border-2 border-zinc-200 p-2 text-zinc-600 outline-none focus:border-blue-600 focus:ring-transparent dark:border-zinc-600 dark:bg-zinc-800 dark:text-zinc-200 dark:focus:border-blue-600 dark:disabled:bg-zinc-600"
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
</div>
