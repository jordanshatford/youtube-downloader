<script lang="ts">
	import moment from 'moment'
	import {
		CheckCircleIcon,
		AlertTriangleIcon,
		AlertCircleIcon,
		InfoIcon
	} from 'svelte-feather-icons'
	import { Variant } from '$lib/utils/types'
	import type { Notification } from '$lib/utils/types'

	export let notification: Notification

	const _types = {
		[Variant.DANGER]: {
			icon: AlertCircleIcon,
			iconClass: 'text-red-800 bg-red-200'
		},
		[Variant.SUCCESS]: {
			icon: CheckCircleIcon,
			iconClass: 'text-green-700 bg-green-200'
		},
		[Variant.WARNING]: {
			icon: AlertTriangleIcon,
			iconClass: 'text-yellow-600 bg-yellow-200'
		},
		[Variant.INFO]: {
			icon: InfoIcon,
			iconClass: 'text-blue-800 bg-blue-200'
		}
	}
</script>

<div class="w-full p-3 mt-4 bg-white rounded flex dark:bg-gray-800">
	<div
		tabindex="0"
		class="{_types[notification.type]
			.iconClass} rounded-full w-8 h-8 flex items-center justify-center"
	>
		<svelte:component this={_types[notification.type].icon} size="4x" class="p-1" />
	</div>
	<div class="pl-3">
		<p tabindex="0" class="focus:outline-none text-sm leading-none dark:text-gray-200">
			{notification.title}
		</p>
		<p
			tabindex="0"
			class="focus:outline-none text-xs leading-3 pt-1 text-gray-600 dark:text-gray-400"
		>
			{notification.message}
		</p>
		<p tabindex="0" class="focus:outline-none text-xs leading-3 pt-1 text-gray-500">
			{moment(notification.time).fromNow()}
		</p>
	</div>
</div>
