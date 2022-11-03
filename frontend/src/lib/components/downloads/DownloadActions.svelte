<script lang="ts">
	import { createEventDispatcher } from 'svelte'
	import { Trash2Icon, DownloadIcon, LoaderIcon } from 'svelte-feather-icons'
	import IconButton from '$lib/components/ui/IconButton.svelte'
	import Confirm from '$lib/components/ui/Confirm.svelte'
	import { Status } from '$lib/utils/types'

	const dispatch = createEventDispatcher()
	export let status: Status
	export let awaitingFileBlob = false
</script>

<div>
	{#if [Status.DONE, Status.ERROR, Status.UNDEFINED].includes(status)}
		<Confirm
			title="Delete Audio?"
			description="Are you sure you want to delete this audio? Deleting is permanent."
			cancelText="Cancel"
			confirmText="Delete"
			let:confirm={onConfirm}
		>
			<IconButton
				on:click={() => onConfirm(dispatch, 'delete')}
				icon={Trash2Icon}
				size="1.5x"
				class="hover:text-red-600 mr-2"
			/>
		</Confirm>
	{/if}
	{#if status === Status.DONE}
		{#if awaitingFileBlob}
			<IconButton icon={LoaderIcon} size="1.5x" class="animate-spin" />
		{:else}
			<IconButton
				on:click={() => dispatch('download')}
				icon={DownloadIcon}
				size="1.5x"
				class="hover:text-indigo-800 dark:hover:text-indigo-600"
			/>
		{/if}
	{/if}
</div>
