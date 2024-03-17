export type VideoFormat = 'avi' | 'flv' | 'mkv' | 'mov' | 'mp4' | 'webm';

export const VideoFormatEnum = {
	AVI: 'avi',
	FLV: 'flv',
	MKV: 'mkv',
	MOV: 'mov',
	MP4: 'mp4',
	WEBM: 'webm'
} as const;
