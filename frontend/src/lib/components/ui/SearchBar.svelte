<script lang="ts">
	import { createEventDispatcher } from 'svelte';
	import { SearchIcon, LoaderIcon } from 'svelte-feather-icons';

	const dispatch = createEventDispatcher();

	export let loading = false;
	export let searchTerm: string;

	function dispatchSearch(event: KeyboardEvent) {
		if (event.key === 'Enter' && searchTerm.length > 0) {
			dispatch('search', { term: searchTerm });
		}
	}
</script>

<div class="w-full">
	<div class="flex">
		<div class="w-10 z-10 pl-1 text-center pointer-events-none flex items-center justify-center">
			{#if loading}
				<LoaderIcon size="1.5x" class="text-zinc-400 animate-spin" />
			{:else}
				<SearchIcon size="1.5x" class="text-zinc-400" />
			{/if}
		</div>
		<input
			disabled={loading}
			bind:value={searchTerm}
			on:keypress={dispatchSearch}
			type="text"
			class="w-full -ml-10 pl-10 pr-3 py-2 text-zinc-600 dark:text-zinc-200 rounded-lg border-2 border-zinc-200 dark:border-zinc-600 outline-none dark:bg-zinc-800 dark:disabled:bg-zinc-600"
			placeholder="search"
		/>
	</div>
</div>
