<script lang="ts">
    import { flip } from "svelte/animate"
    import { fly } from "svelte/transition"
    import { notifications } from "../stores/notifications"
    import Icon from "./Icon.svelte"
    import { checkCircle, informationCircle, exclamationCircle, exclamationTriangle } from "./icons"

    export const themes = {
        danger: {
          icon: exclamationCircle,
          iconClass: "text-red-800",
        },
        success: {
          icon: checkCircle,
          iconClass: "text-green-700",
        },
        warning: {
          icon: exclamationTriangle,
          iconClass: "text-yellow-600",
        },
        info: {
          icon: informationCircle,
          iconClass: "text-blue-800",
        },
    }
</script>

<div class="flex flex-col justify-start m-auto fixed mt-20 top-0 right-0 z-50 pointer-events-none">
    {#each $notifications as notification (notification.id)}
    <div
        animate:flip
        transition:fly={{ y: 30 }}
        class="flex-auto bg-white dark:bg-gray-900 rounded-lg border-gray-300 dark:border-gray-700 mb-2 mr-2 border p-3 shadow-lg"
    >
        <div class="flex flex-row">
            <Icon data={themes[notification.type].icon} size={3} className="px-2 {themes[notification.type].iconClass}" />
            <div class="ml-2 mr-6">
                <span class="font-semibold text-gray-900 dark:text-white">{ notification.title }</span>
                <span class="block text-gray-500 dark:text-gray-400">{ notification.message }</span>
            </div>
        </div>
    </div>
    {/each}
</div>
