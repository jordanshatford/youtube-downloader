<script lang="ts">
    import Icon from "./Icon.svelte"

    export let data: string
    export let size: number = 1
    export let className: string = ""
</script>

<button
    on:click
    class="{className} rounded-md border-none focus:outline-none p-2"
    type="button"
>
    <Icon {data} {size} />
</button>
