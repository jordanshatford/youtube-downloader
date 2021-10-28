import { writable } from 'svelte/store'
import { Variant } from '$lib/utils/types'
import type { Notification } from '$lib/utils/types'

function createNotificationsStore() {
	const _notifications: Notification[] = []

	const { subscribe, set, update } = writable({
		visible: false,
		values: _notifications
	})

	function id() {
		return '_' + Math.random().toString(36).substr(2, 9)
	}

	function send(title: string, msg: string, type: Variant) {
		update((state) => {
			const notification: Notification = {
				id: id(),
				time: new Date(),
				title,
				message: msg,
				type
			}
			state.values = [notification, ...state.values]
			return state
		})
	}

	function toggleVisible() {
		update((state) => {
			state.visible = !state.visible
			return state
		})
	}

	return {
		subscribe,
		send,
		danger: (title: string, msg: string) => send(title, msg, Variant.DANGER),
		warning: (title: string, msg: string) => send(title, msg, Variant.WARNING),
		info: (title: string, msg: string) => send(title, msg, Variant.INFO),
		success: (title: string, msg: string) => send(title, msg, Variant.SUCCESS),
		toggleVisible,
		reset: () => set({ visible: false, values: _notifications })
	}
}

export const notifications = createNotificationsStore()
