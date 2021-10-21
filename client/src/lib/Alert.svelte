<script lang="ts">
    import Icon from "./Icon.svelte"
    import { checkCircle, informationCircle, exclamationCircle, exclamationTriangle } from "./icons"
    import { Variant } from '../utils/types'

    export let variant: Variant
    export let title: string
    export let message: string

    const themes = {
        [Variant.DANGER]: {
            icon: exclamationCircle,
            class: "text-red-800 bg-red-200",
        },
        [Variant.SUCCESS]: {
            icon: checkCircle,
            class: "text-green-700 bg-green-200",
        },
        [Variant.WARNING]: {
            icon: exclamationTriangle,
            class: "text-yellow-600 bg-yellow-200",
        },
        [Variant.INFO]: {
            icon: informationCircle,
            class: "text-blue-800 bg-blue-200",
        },
    }
</script>

<div class="{themes[variant].class} shadow rounded-md md:flex justify-between items-center top-0 py-2 px-2">
    <div class="sm:flex items-center">
        <div class="flex items-end">
            <Icon data={themes[variant].icon} size={2} className="{themes[variant].class}" />
            <p class="mb-1 mx-2 font-bold {themes[variant].class}">{title}</p>
        </div>
        <p class="pl-2 md:pl-0">{message}</p>
    </div>
</div>

        