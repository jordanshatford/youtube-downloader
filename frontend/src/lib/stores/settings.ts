import { browser } from '$app/env'
import { writable } from 'svelte/store'
import type { AudioSettings } from '$lib/utils/types'
import { AudioFormat } from '$lib/utils/types'

function createSettingsStore() {
	const SETTINGS_KEY = 'settings'
	const DEFAULT_SETTINGS: AudioSettings = {
		format: AudioFormat.MP3
	}

	const { subscribe, set, update } = writable(DEFAULT_SETTINGS)

	if (browser) {
		const data = localStorage?.getItem(SETTINGS_KEY)
		const parsedData = JSON.parse(data) as AudioSettings

		if (parsedData) {
			set(parsedData)
		}
	}

	subscribe((value) => {
		if (browser) {
			const settingsJsonString = JSON.stringify(value)
			localStorage?.setItem(SETTINGS_KEY, settingsJsonString)
		}
	})

	return {
		subscribe,
		set,
		update,
		reset: () => set(DEFAULT_SETTINGS)
	}
}

export const settings = createSettingsStore()
