<script lang="ts">
	import { createEventDispatcher } from 'svelte'
	import Icon from '$lib/components/Icon.svelte'
	import Spinner from '$lib/components/Spinner.svelte'
	import { search } from '$lib/components/icons'

	const dispatch = createEventDispatcher()

	export let loading = false

	export let searchTerm: string

	function dispatchSearch(event: KeyboardEvent) {
		if (event.key === 'Enter' && searchTerm.length > 0) {
			dispatch('search', { term: searchTerm })
		}
	}
</script>

<div>
	{#if loading}
		<Spinner className="absolute text-gray-400 top-10 left-4" />
	{:else}
		<Icon data={search} className="absolute text-gray-400 top-10 left-4" />
	{/if}
	<input
		disabled={loading}
		bind:value={searchTerm}
		on:keypress={dispatchSearch}
		type="text"
		class="border border-gray-400 dark:text-gray-400 dark:border-gray-700 bg-white dark:bg-gray-900 disabled:text-gray-200 h-14 w-full px-12 rounded-lg focus:outline-none"
		name=""
	/>
</div>
