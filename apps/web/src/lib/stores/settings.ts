import { writable } from 'svelte/store';
import { AudioFormat, DownloadQuality, type AudioOptions } from '@yd/client';
import { browser } from '$app/environment';

function createSettingsStore() {
	const SETTINGS_KEY = 'settings';
	const DEFAULT_SETTINGS: AudioOptions = {
		format: AudioFormat.MP3,
		quality: DownloadQuality.BEST
	};

	const { subscribe, set, update } = writable(DEFAULT_SETTINGS);

	if (browser) {
		const data = localStorage?.getItem(SETTINGS_KEY);

		if (data !== null) {
			const parsedData = JSON.parse(data) as AudioOptions;
			// Make sure a value is set, if nothing is set use the default
			if (!Object.values(AudioFormat).includes(parsedData.format)) {
				parsedData.format = DEFAULT_SETTINGS.format;
			}
			if (!Object.values(DownloadQuality).includes(parsedData.quality)) {
				parsedData.quality = DEFAULT_SETTINGS.quality;
			}
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
