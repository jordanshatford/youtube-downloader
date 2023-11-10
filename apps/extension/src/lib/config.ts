export const env = {
	serverAddress: (import.meta.env.VITE_SERVER_ADDR ?? 'http://localhost:8080') as string
};

export const config = {
	website: 'https://youtubedownloader.duckdns.org',
	github: 'https://github.com/jordanshatford/youtube-downloader',
	copyright: {
		owner: 'Jordan Shatford',
		year: 2022
	}
};

export default config;
