import type { AudioFormat } from './AudioFormat';
import type { DownloadQuality } from './DownloadQuality';
import type { VideoFormat } from './VideoFormat';

export type AvailableDownloadOptions = {
	format: Array<AudioFormat | VideoFormat>;
	quality: Array<DownloadQuality>;
	embed_metadata: Array<boolean>;
	embed_thumbnail: Array<boolean>;
	embed_subtitles: Array<boolean>;
};
