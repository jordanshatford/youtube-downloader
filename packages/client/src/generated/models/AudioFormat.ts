export type AudioFormat = 'aac' | 'flac' | 'm4a' | 'mp3' | 'opus' | 'wav';

export const AudioFormatEnum = {
	AAC: 'aac',
	FLAC: 'flac',
	M4A: 'm4a',
	MP3: 'mp3',
	OPUS: 'opus',
	WAV: 'wav'
} as const;
