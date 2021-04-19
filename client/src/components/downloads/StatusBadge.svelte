<script>
    import Icon from "svelte-awesome"
    import { circleONotch } from "svelte-awesome/icons"
    import { Status } from "../../utils/enums.js"

    export let statusValue

    let className

    $: switch(statusValue) {
        case Status.WAITING:
            className = "bg-yellow-100 text-yellow-800"
            break
        case Status.DOWNLOADING:
            className = "bg-gray-100 text-gray-800"
            break
        case Status.PROCESSING:
            className = "bg-gray-100 text-gray-800"
            break
        case Status.DONE:
            className = "bg-green-100 text-green-800"
            break
        default: // STATUS.UNDEFINED
            statusValue = Status.UNDEFINED
            className = "bg-red-100 text-red-800"
            break
    }
</script>

<span class="content-center px-3 py-2 text-xs font-semibold rounded-full {className}">
    {statusValue}
    {#if [Status.DOWNLOADING, Status.PROCESSING].includes(statusValue)}
    <Icon data={circleONotch} spin />
    {/if}
</span>