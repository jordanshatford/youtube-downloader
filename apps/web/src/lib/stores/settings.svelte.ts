import { browser } from '$app/environment';

import type { DownloadOptions } from '@yd/client';
import { AudioFormat, DEFAULT_DOWNLOAD_OPTIONS, DownloadQuality, VideoFormat } from '@yd/client';

const SETTINGS_KEY = 'yd-settings';

class SettingsStore {
	public settings = $state<DownloadOptions>(DEFAULT_DOWNLOAD_OPTIONS);

	public constructor() {
		if (browser) {
			const data = localStorage?.getItem(SETTINGS_KEY);
			if (data !== null) {
				const parsedData = JSON.parse(data) as DownloadOptions;
				const supportedFormats = [...Object.values(AudioFormat), ...Object.values(VideoFormat)];
				// Make sure a value is set, if nothing is set use the default
				if (!supportedFormats.includes(parsedData.format)) {
					parsedData.format = DEFAULT_DOWNLOAD_OPTIONS.format;
				}
				if (!Object.values(DownloadQuality).includes(parsedData.quality)) {
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
				this.settings = parsedData;
			}
		}
		// Watch changes and sync in local storage.
		$effect.root(() => {
			$effect(() => {
				localStorage.setItem(SETTINGS_KEY, JSON.stringify(this.settings));
			});
			return () => {};
		});
	}

	public reset() {
		this.settings = DEFAULT_DOWNLOAD_OPTIONS;
	}
}

export const settings = new SettingsStore();

const USER_SETTINGS_KEY = 'yd-usersettings';
const DEFAULT_USER_SETTINGS = {
	autoDownloadOnComplete: false,
	downloadsPageSize: 10
};

class UserSettingsStore {
	public settings = $state(DEFAULT_USER_SETTINGS);

	public constructor() {
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
				this.settings = parsedData;
			}
		}
		// Watch changes and sync in local storage.
		$effect.root(() => {
			$effect(() => {
				localStorage.setItem(USER_SETTINGS_KEY, JSON.stringify(this.settings));
			});
			return () => {};
		});
	}

	public reset() {
		this.settings = DEFAULT_USER_SETTINGS;
	}
}

export const userSettings = new UserSettingsStore();
