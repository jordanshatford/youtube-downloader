<script lang="ts">
	import { notifications } from '$lib/stores/notifications'
	import { XIcon, BellOffIcon } from 'svelte-feather-icons'
	import IconButton from '$lib/components/ui/IconButton.svelte'
	import Notification from '$lib/components/ui/Notification.svelte'

	export let visible = false
</script>

{#if visible}
	<div
		class="cursor-pointer w-full h-full bg-gray-800 bg-opacity-75 top-0 overflow-y-auto overflow-x-hidden fixed sticky-0 z-40"
		id="chec-div"
	>
		<div
			on:click={() => notifications.toggleVisible()}
			class="w-full absolute z-10 right-0 h-full overflow-x-hidden transform translate-x-0 transition ease-in-out duration-700"
			id="notification"
		>
			<div
				class="xl:w-1/3 lg:w-5/12 md:w-3/5 sm:w-2/3 w-10/12 bg-gray-50 dark:bg-gray-900 h-screen overflow-y-auto px-8 py-4 absolute right-0"
			>
				<div class="flex items-center justify-between">
					<p
						tabindex="0"
						class="focus:outline-none text-2xl font-semibold leading-6 text-gray-800 dark:text-gray-200"
					>
						Notifications
					</p>
					<IconButton
						class="dark:text-gray-200 hover:text-red-800 dark:hover:text-red-600"
						on:click={() => notifications.toggleVisible()}
						icon={XIcon}
						size="1.5x"
					/>
				</div>
				{#each $notifications.values as notification (notification.id)}
					<Notification {notification} />
				{:else}
					<div class="w-full p-3 mt-4 bg-white rounded flex dark:bg-gray-800">
						<div
							tabindex="0"
							class="rounded-full w-8 h-8 flex items-center justify-center dark:text-gray-200"
						>
							<svelte:component this={BellOffIcon} size="4x" class="p-1" />
						</div>
						<div class="pl-3 dark:text-gray-200">No notifications</div>
					</div>
				{/each}
			</div>
		</div>
	</div>
{/if}
