<script lang="ts">
	import { BellIcon } from 'svelte-feather-icons'
	import IconButton from '$lib/components/ui/IconButton.svelte'
	import { notifications } from '$lib/stores/notifications'

	let className = ''
	export { className as class }
	export let size = '1.5x'
</script>

<span class="relative inline-block">
	<IconButton
		on:click={() => notifications.toggleVisible()}
		class="{className} hover:text-indigo-800 dark:hover:text-indigo-600 text-gray-500 dark:text-gray-200 dark:bg-gray-800"
		icon={BellIcon}
		{size}
	/>
	{#if $notifications?.values?.length > 0}
		<span
			class="absolute z-30 top-0 right-0 inline-flex items-center justify-center px-2 py-1 text-xs font-bold leading-none text-red-100 transform translate-x-1/2 -translate-y-1/2 bg-red-600 rounded-full"
			>{$notifications.values.length}</span
		>
	{/if}
</span>
