import type { DownloadOptions } from './DownloadOptions';
import type { DownloadStatus } from './DownloadStatus';
import type { Video } from './Video';

export type Download = {
	video: Video;
	options: DownloadOptions;
	status: DownloadStatus;
};
