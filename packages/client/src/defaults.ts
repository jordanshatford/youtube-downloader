import type { DownloadOptions } from './generated';

// Default download options to use on various platforms.
export const DEFAULT_DOWNLOAD_OPTIONS: DownloadOptions = {
	format: 'mp4',
	quality: 'best',
	embed_metadata: true,
	embed_thumbnail: false,
	embed_subtitles: false
};
