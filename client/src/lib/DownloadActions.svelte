<script lang="ts">
	import Confirm from "./Confirm.svelte"
	import IconButton from "./IconButton.svelte"
    import { trash, download, edit } from "./icons"
    import { createEventDispatcher } from "svelte"

    const dispatch = createEventDispatcher()
</script>

<Confirm
    title="Delete Song?"
    description="Are you sure you want to delete this song? Deleting is permanent."
    cancelTitle="Cancel"
    confirmTitle="Delete"
    let:confirm="{confirmThis}"
>
    <IconButton
        className="hover:text-red-500"
        size={1.25}
        data={trash}
        on:click={_ => confirmThis(dispatch, "delete")}
    />
</Confirm> 
<IconButton
    className="hover:text-purple-500"
    size={1.25}
    data={download}
    on:click={_ => dispatch("download")}
/>