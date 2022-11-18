import { AudioFormat, Theme } from '$lib/utils/types'

export const env = {
	serverAddress: import.meta.env.VITE_SERVER_ADDR as string
}

const config = {
	app: {
		title: 'Youtube Audio Downloader',
		hostname: 'youtubeaudiodownloader.vercel.app',
		creator: 'Jordan Shatford',
		github: 'https://github.com/jordanshatford/youtube-to-mp3',
		year: 2022
	},
	settings: {
		key: 'settings',
		defaults: {
			format: AudioFormat.MP3
		}
	},
	theme: {
		key: 'theme',
		default: Theme.DARK
	}
}

export default config
