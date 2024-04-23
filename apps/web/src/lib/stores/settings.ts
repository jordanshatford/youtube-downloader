import { browser } from '$app/environment';
import { writable } from 'svelte/store';

import type { DownloadOptions } from '@yd/client';
import {
	AudioFormatEnum,
	DEFAULT_DOWNLOAD_OPTIONS,
	DownloadQualityEnum,
	VideoFormatEnum
} from '@yd/client';

const SETTINGS_KEY = 'yd-settings';

function createSettingsStore() {
	const { subscribe, set, update } = writable(DEFAULT_DOWNLOAD_OPTIONS);

	if (browser) {
		const data = localStorage?.getItem(SETTINGS_KEY);

		if (data !== null) {
			const parsedData = JSON.parse(data) as DownloadOptions;
			const supportedFormats = [
				...Object.values(AudioFormatEnum),
				...Object.values(VideoFormatEnum)
			];
			// Make sure a value is set, if nothing is set use the default
			if (!supportedFormats.includes(parsedData.format)) {
				parsedData.format = DEFAULT_DOWNLOAD_OPTIONS.format;
			}
			if (!Object.values(DownloadQualityEnum).includes(parsedData.quality)) {
				parsedData.quality = DEFAULT_DOWNLOAD_OPTIONS.quality;
			}
			if (parsedData.embed_metadata === undefined) {
				parsedData.embed_metadata = DEFAULT_DOWNLOAD_OPTIONS.embed_metadata;
			}
			if (parsedData.embed_thumbnail === undefined) {
				parsedData.embed_thumbnail = DEFAULT_DOWNLOAD_OPTIONS.embed_thumbnail;
			}
			if (parsedData.embed_subtitles === undefined) {
				parsedData.embed_subtitles = DEFAULT_DOWNLOAD_OPTIONS.embed_subtitles;
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
		reset: () => set(DEFAULT_DOWNLOAD_OPTIONS)
	};
}

export const settings = createSettingsStore();

function createUserSettingsStore() {
	const USER_SETTINGS_KEY = 'yd-usersettings';
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
