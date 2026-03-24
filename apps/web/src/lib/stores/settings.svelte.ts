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
				if (parsed.embed_metadata !== undefined && typeof parsed.embed_metadata === "boolean") {
					this.settings.embed_metadata = parsed.embed_metadata;
				}
				if (parsed.embed_thumbnail !== undefined && typeof parsed.embed_thumbnail === "boolean") {
					this.settings.embed_thumbnail = parsed.embed_thumbnail;
				}
				if (parsed.embed_subtitles !== undefined && typeof parsed.embed_subtitles === "boolean") {
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
