<script lang="ts">
    import Icon from "svelte-awesome"

    export let data: any
    export let iconScale: number
    export let className: string
    export let disabled: boolean
</script>

<button
    on:click
    {disabled}
    class="{className} text-white p-1 rounded-md border-none focus:outline-none disabled:opacity-50 disabled:text-gray-500 disabled:cursor-default"
    type="button"
>
    <Icon {data} scale={iconScale} />
</button>