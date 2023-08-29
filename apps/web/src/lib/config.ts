import { AudioFormat } from '$lib/utils/types';

export const env = {
	serverAddress: import.meta.env.VITE_SERVER_ADDR as string
};

const config = {
	about: {
		title: 'YouTube Audio Downloader',
		hostname: 'youtubeaudiodownloader.vercel.app'
	},
	settings: {
		key: 'settings',
		defaults: {
			format: AudioFormat.MP3
		}
	},
	github: 'https://github.com/jordanshatford/youtube-audio-downloader',
	copyright: {
		owner: 'Jordan Shatford',
		year: 2022
	}
};

export default config;
