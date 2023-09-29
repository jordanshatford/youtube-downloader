import { writable } from 'svelte/store';
import {
	AudioFormat,
	DownloadQuality,
	type DownloadOptions,
	DownloadType,
	VideoFormat
} from '@yd/client';
import { browser } from '$app/environment';

function createSettingsStore() {
	const SETTINGS_KEY = 'settings';
	const DEFAULT_SETTINGS: DownloadOptions = {
		type: DownloadType.AUDIO,
		format: AudioFormat.MP3,
		quality: DownloadQuality.BEST,
		embed_metadata: true
	};
	const DEFAULT_VIDEO_FORMAT: VideoFormat = VideoFormat.MP4;

	const { subscribe, set, update } = writable(DEFAULT_SETTINGS);

	if (browser) {
		const data = localStorage?.getItem(SETTINGS_KEY);

		if (data !== null) {
			const parsedData = JSON.parse(data) as DownloadOptions;
			// Make sure value is set for type
			if (!Object.values(DownloadType).includes(parsedData.type)) {
				parsedData.type = DEFAULT_SETTINGS.type;
			}
			// Make sure a value is set, if nothing is set use the default
			if (
				parsedData.type === DownloadType.AUDIO &&
				!Object.values(AudioFormat).includes(parsedData.format as AudioFormat)
			) {
				parsedData.format = DEFAULT_SETTINGS.format;
			}

			if (
				parsedData.type === DownloadType.VIDEO &&
				!Object.values(VideoFormat).includes(parsedData.format as VideoFormat)
			) {
				parsedData.format = DEFAULT_VIDEO_FORMAT;
			}

			if (!Object.values(DownloadQuality).includes(parsedData.quality)) {
				parsedData.quality = DEFAULT_SETTINGS.quality;
			}
			if (parsedData.embed_metadata == undefined) {
				parsedData.embed_metadata = DEFAULT_SETTINGS.embed_metadata;
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

function createUserSettingsStore() {
	const USER_SETTINGS_KEY = 'userSettings';
	const DEFAULT_USER_SETTINGS = {
		autoDownloadOnComplete: false
	};

	const { subscribe, set, update } = writable(DEFAULT_USER_SETTINGS);

	if (browser) {
		const data = localStorage?.getItem(USER_SETTINGS_KEY);
		if (data !== null) {
			const parsedData = JSON.parse(data) as typeof DEFAULT_USER_SETTINGS;
			set(parsedData);
		}
	}

	subscribe((value) => {
		if (browser) {
			localStorage?.setItem(USER_SETTINGS_KEY, JSON.stringify(value));
		}
	});

	return {
		subscribe,
		set,
		update,
		reset: () => set(DEFAULT_USER_SETTINGS)
	};
}

export const userSettings = createUserSettingsStore();
