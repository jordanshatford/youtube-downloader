<script lang="ts">
	import IconButton from "./IconButton.svelte";
    import { trash, download } from "../lib/icons"
    import { createEventDispatcher } from "svelte"

    const dispatch = createEventDispatcher()
</script>

<IconButton
    className="hover:text-red-500 hover:scale-110"
    size={1.25}
    data={trash}
    on:click={_ => dispatch("delete")}
/>
<IconButton
    className="hover:text-purple-500 hover:scale-110"
    size={1.25}
    data={download}
    on:click={_ => dispatch("download")}
/>