<script lang="ts">
	import Confirm from "../Confirm.svelte"
	import IconButton from "../IconButton.svelte"
    import { createEventDispatcher } from "svelte"
    import { trash, download } from "../icons"

    const dispatch = createEventDispatcher()
</script>

<div>
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
</div>