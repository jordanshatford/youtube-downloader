import { browser } from '$app/environment';

import type { DownloadOptions } from '@yd/client';
import {
	AudioFormat,
	DownloadQuality,
	getDownloadsOptionsDefaults,
	LanguageCode,
	VideoFormat
} from '@yd/client';

const SETTINGS_KEY = 'yd-settings';

class SettingsStore {
	public settings = $state<DownloadOptions>({} as DownloadOptions);

	public async init() {
		if (browser) {
			// Set the default values based on server.
			const { data: defaults } = await getDownloadsOptionsDefaults();
			if (defaults) {
				this.settings = defaults;
			}
			// Override settings values with those that are in local storage if they are valid.
			// Otherwise they will remain the default provided by the server.
			const data = localStorage?.getItem(SETTINGS_KEY);
			if (data !== null) {
				const parsed = JSON.parse(data) as DownloadOptions;
				// Make sure a value is set, if nothing is set use the default
				if (
					parsed.format &&
					[...Object.values(AudioFormat), ...Object.values(VideoFormat)].includes(parsed.format)
				) {
					this.settings.format = parsed.format;
				}
				if (parsed.quality && Object.values(DownloadQuality).includes(parsed.quality)) {
					this.settings.quality = parsed.quality;
				}
				if (parsed.embed_metadata !== undefined) {
					this.settings.embed_metadata = parsed.embed_metadata;
				}
				if (parsed.embed_thumbnail !== undefined) {
					this.settings.embed_thumbnail = parsed.embed_thumbnail;
				}
				if (parsed.embed_subtitles !== undefined) {
					this.settings.embed_subtitles = parsed.embed_subtitles;
				}
				if (
					parsed.preferred_subtitles_language &&
					Object.values(LanguageCode).includes(parsed.preferred_subtitles_language)
				) {
					this.settings.preferred_subtitles_language = parsed.preferred_subtitles_language;
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
