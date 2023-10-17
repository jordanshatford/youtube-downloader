import { writable } from 'svelte/store';
import { AudioFormat, DownloadQuality, type DownloadOptions, VideoFormat } from '@yd/client';
import { browser } from '$app/environment';

function createSettingsStore() {
	const SETTINGS_KEY = 'settings';
	const DEFAULT_SETTINGS: DownloadOptions = {
		format: VideoFormat.MP4,
		quality: DownloadQuality.BEST,
		embed_metadata: false,
		embed_thumbnail: false,
		embed_subtitles: false
	};

	const { subscribe, set, update } = writable(DEFAULT_SETTINGS);

	if (browser) {
		const data = localStorage?.getItem(SETTINGS_KEY);

		if (data !== null) {
			const parsedData = JSON.parse(data) as DownloadOptions;
			const supportedFormats = [...Object.values(AudioFormat), ...Object.values(VideoFormat)];
			// Make sure a value is set, if nothing is set use the default
			if (!supportedFormats.includes(parsedData.format)) {
				parsedData.format = DEFAULT_SETTINGS.format;
			}
			if (!Object.values(DownloadQuality).includes(parsedData.quality)) {
				parsedData.quality = DEFAULT_SETTINGS.quality;
			}
			if (parsedData.embed_metadata == undefined) {
				parsedData.embed_metadata = DEFAULT_SETTINGS.embed_metadata;
			}
			if (parsedData.embed_thumbnail == undefined) {
				parsedData.embed_thumbnail = DEFAULT_SETTINGS.embed_thumbnail;
			}
			if (parsedData.embed_subtitles == undefined) {
				parsedData.embed_subtitles = DEFAULT_SETTINGS.embed_subtitles;
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
		autoDownloadOnComplete: false,
		downloadsPageSize: 10
	};

	const { subscribe, set, update } = writable(DEFAULT_USER_SETTINGS);

	if (browser) {
		const data = localStorage?.getItem(USER_SETTINGS_KEY);
		if (data !== null) {
			const parsedData = JSON.parse(data) as typeof DEFAULT_USER_SETTINGS;
			if (
				!parsedData.downloadsPageSize ||
				Number.isNaN(parsedData.downloadsPageSize) ||
				Number(parsedData.downloadsPageSize) < 1
			) {
				parsedData.downloadsPageSize = DEFAULT_USER_SETTINGS.downloadsPageSize;
			}
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
