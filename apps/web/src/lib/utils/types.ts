// The status of a video being converted to MP3
export enum Status {
	WAITING = 'WAITING',
	DOWNLOADING = 'DOWNLOADING',
	PROCESSING = 'PROCESSING',
	DONE = 'DONE',
	ERROR = 'ERROR',
	UNDEFINED = 'UNDEFINED'
}

export type Variant = 'default' | 'info' | 'success' | 'warning' | 'danger';

export enum AudioFormat {
	MP3 = 'mp3',
	AAC = 'aac',
	FLAC = 'flac',
	M4A = 'm4a',
	OPUS = 'opus',
	WAV = 'wav'
}

export type AudioSettings = {
	format: AudioFormat;
};

export type ListItem = {
	title: string;
	description?: string;
};

export type ChannelInfo = {
	name: string;
	url?: string;
	thumbnail?: string;
};

export type VideoInfo = {
	id: string;
	url: string;
	title: string;
	thumbnail: string;
	duration?: string;
	channel?: ChannelInfo;
	status?: Status;
	options?: AudioSettings;
	awaitingFileBlob?: boolean;
};
