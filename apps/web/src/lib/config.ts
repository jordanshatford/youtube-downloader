export const env = {
	serverAddress: (import.meta.env.VITE_SERVER_ADDR ?? 'http://localhost:8080') as string
};

const config = {
	about: {
		hostname: 'youtubedownloader.duckdns.org'
	},
	head: {
		title: 'YouTube Downloader',
		description:
			'YouTube Downloader is a fast and free online tool to download and convert YouTube videos to various audio or video formats.',
		url: 'https://youtubedownloader.duckdns.org',
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
		year: new Date().getFullYear()
	}
};

export default config;
