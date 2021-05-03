<script lang="ts">
    import Icon from "svelte-awesome"
    import { circleONotch, check, exclamationCircle } from "svelte-awesome/icons"

    import { Status } from "../../utils/types"

    export let status: Status

    let className: string
    let icon: any = circleONotch

    $: switch(status) {
        case Status.WAITING:
            className = "bg-yellow-100 text-yellow-800"
            break
        case Status.DOWNLOADING:
            className = "bg-blue-100 text-blue-800"
            break
        case Status.PROCESSING:
            className = "bg-purple-100 text-purple-800"
            break
        case Status.DONE:
            className = "bg-green-100 text-green-800"
            icon = check
            break
        default: // STATUS.UNDEFINED
            status = Status.UNDEFINED
            className = "bg-red-100 text-red-800"
            icon = exclamationCircle
            break
    }
</script>

<span class="content-center px-3 py-2 text-xs font-semibold rounded-full {className}">
    {status}
    <Icon data={icon} spin={[Status.WAITING, Status.DOWNLOADING, Status.PROCESSING].includes(status)} class="mb-1" />
</span>