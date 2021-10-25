<script lang="ts">
	import Confirm from '$lib/components/Confirm.svelte'
	import IconButton from '$lib/components/IconButton.svelte'
	import { createEventDispatcher } from 'svelte'
	import { trash, download } from '$lib/components/icons'

	const dispatch = createEventDispatcher()
</script>

<div>
	<Confirm
		title="Delete Audio?"
		description="Are you sure you want to delete this audio? Deleting is permanent."
		cancelText="Cancel"
		confirmText="Delete"
		let:confirm={onConfirm}
	>
		<IconButton
			className="hover:text-red-500"
			size={1.25}
			data={trash}
			on:click={() => onConfirm(dispatch, 'delete')}
		/>
	</Confirm>
	<IconButton
		className="hover:text-purple-500"
		size={1.25}
		data={download}
		on:click={() => dispatch('download')}
	/>
</div>
