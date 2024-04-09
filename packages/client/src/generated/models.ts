export type AudioFormat = 'aac' | 'flac' | 'm4a' | 'mp3' | 'opus' | 'wav';

export const AudioFormatEnum = {
	AAC: 'aac',
	FLAC: 'flac',
	M4A: 'm4a',
	MP3: 'mp3',
	OPUS: 'opus',
	WAV: 'wav'
} as const;

export type AvailableDownloadOptions = {
	format: Array<AudioFormat | VideoFormat>;
	quality: Array<DownloadQuality>;
	embed_metadata: Array<boolean>;
	embed_thumbnail: Array<boolean>;
	embed_subtitles: Array<boolean>;
};

export type Channel = {
	name: string;
	url: string;
	thumbnail: string;
};

export type Download = {
	video: Video;
	options: DownloadOptions;
	status: DownloadStatus;
};

export type DownloadInput = {
	video: Video;
	options: DownloadOptions;
};

export type DownloadOptions = {
	format: AudioFormat | VideoFormat;
	quality: DownloadQuality;
	embed_metadata: boolean;
	embed_thumbnail: boolean;
	embed_subtitles: boolean;
};

export type DownloadQuality = 'best' | 'worst';

export const DownloadQualityEnum = {
	BEST: 'best',
	WORST: 'worst'
} as const;

export type DownloadState = 'WAITING' | 'DOWNLOADING' | 'PROCESSING' | 'DONE' | 'ERROR';

export const DownloadStateEnum = {
	WAITING: 'WAITING',
	DOWNLOADING: 'DOWNLOADING',
	PROCESSING: 'PROCESSING',
	DONE: 'DONE',
	ERROR: 'ERROR'
} as const;

export type DownloadStatus = {
	state: DownloadState;
	downloaded_bytes?: number | null;
	total_bytes?: number | null;
	elapsed?: number | null;
	eta?: number | null;
	speed?: number | null;
	postprocessor?: string | null;
	readonly progress: number | null;
};

export type HTTPValidationError = {
	detail?: Array<ValidationError>;
};

export type Session = {
	id: string;
};

export type ValidationError = {
	loc: Array<string | number>;
	msg: string;
	type: string;
};

export type Video = {
	id: string;
	url: string;
	title: string;
	duration: string;
	thumbnail: string;
	channel: Channel;
};

export type VideoFormat = 'avi' | 'flv' | 'mkv' | 'mov' | 'mp4' | 'webm';

export const VideoFormatEnum = {
	AVI: 'avi',
	FLV: 'flv',
	MKV: 'mkv',
	MOV: 'mov',
	MP4: 'mp4',
	WEBM: 'webm'
} as const;

export type SearchData = {
	payloads: {
		GetSearch: {
			query: string;
		};
		GetVideo: {
			id: string;
		};
	};

	responses: {
		GetSearch: Array<Video>;
		GetNextSearch: Array<Video>;
		GetVideo: Video;
	};
};

export type SessionData = {
	responses: {
		GetSession: Session;
		DeleteSession: void;
		GetSessionValidate: Session;
	};
};

export type DownloadsData = {
	payloads: {
		PutDownloads: {
			requestBody: DownloadInput;
		};
		PostDownloads: {
			requestBody: DownloadInput;
		};
		GetDownload: {
			downloadId: string;
		};
		DeleteDownload: {
			downloadId: string;
		};
		GetDownloadFile: {
			downloadId: string;
		};
	};

	responses: {
		GetDownloads: Array<Download>;
		PutDownloads: Download;
		PostDownloads: Download;
		GetDownloadsOptions: AvailableDownloadOptions;
		GetDownload: Download;
		DeleteDownload: void;
		GetDownloadFile: Blob | File;
	};
};
