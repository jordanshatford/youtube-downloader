import { type DownloadOptions, DownloadQuality, VideoFormat } from './generated';

// Default download options to use on various platforms.
export const DEFAULT_DOWNLOAD_OPTIONS: DownloadOptions = {
	format: VideoFormat.MP4,
	quality: DownloadQuality.BEST,
	embed_metadata: true,
	embed_thumbnail: false,
	embed_subtitles: false
};
