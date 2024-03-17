import { type DownloadOptions, DownloadQualityEnum, VideoFormatEnum } from './generated';

// Default download options to use on various platforms.
export const DEFAULT_DOWNLOAD_OPTIONS: DownloadOptions = {
	format: VideoFormatEnum.MP4,
	quality: DownloadQualityEnum.BEST,
	embed_metadata: true,
	embed_thumbnail: false,
	embed_subtitles: false
};
