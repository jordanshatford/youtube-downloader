<script lang="ts">
    import Icon from "svelte-awesome"

    export let data: any
    export let scale: number
    export let className: string = ""
</script>

<button
    on:click
    class="{className} rounded-md border-none focus:outline-none p-2"
    type="button"
>
    <Icon {data} {scale} />
</button>
