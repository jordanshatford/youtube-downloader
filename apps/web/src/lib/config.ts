export const env = {
	serverAddress: (import.meta.env.VITE_SERVER_ADDR ?? 'http://localhost:8080') as string
};

const config = {
	about: {
		hostname: 'youtubeaudiodownloader.vercel.app'
	},
	head: {
		title: 'YouTube Downloader',
		description:
			'YouTube Downloader is a fast and free online tool to download and convert YouTube videos to various audio or video formats.',
		url: 'https://youtubeaudiodownloader.vercel.app/',
		keywords: [
			'YouTube Downloader',
			'YouTube Converter',
			'YouTube',
			'MP3',
			'music',
			'audio',
			'video'
		]
	},
	github: 'https://github.com/jordanshatford/youtube-downloader',
	copyright: {
		owner: 'Jordan Shatford',
		year: 2022
	}
};

export default config;
