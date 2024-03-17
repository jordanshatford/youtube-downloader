export type DownloadState = 'WAITING' | 'DOWNLOADING' | 'PROCESSING' | 'DONE' | 'ERROR';

export const DownloadStateEnum = {
	WAITING: 'WAITING',
	DOWNLOADING: 'DOWNLOADING',
	PROCESSING: 'PROCESSING',
	DONE: 'DONE',
	ERROR: 'ERROR'
} as const;
