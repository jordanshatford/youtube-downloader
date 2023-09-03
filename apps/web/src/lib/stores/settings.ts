import { writable } from 'svelte/store';
import { AudioFormat, type AudioOptions } from '@yd/client';
import { browser } from '$app/environment';

function createSettingsStore() {
	const SETTINGS_KEY = 'settings';
	const DEFAULT_SETTINGS: AudioOptions = {
		format: AudioFormat.MP3
	};

	const { subscribe, set, update } = writable(DEFAULT_SETTINGS);

	if (browser) {
		const data = localStorage?.getItem(SETTINGS_KEY);

		if (data !== null) {
			const parsedData = JSON.parse(data) as AudioOptions;
			set(parsedData);
		}
	}

	subscribe((value) => {
		if (browser) {
			const settingsJsonString = JSON.stringify(value);
			localStorage?.setItem(SETTINGS_KEY, settingsJsonString);
		}
	});

	return {
		subscribe,
		set,
		update,
		reset: () => set(DEFAULT_SETTINGS)
	};
}

export const settings = createSettingsStore();
