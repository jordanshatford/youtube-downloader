export class RoutePathConstants {
	public static SEARCH = '/'
	public static DOWNLOADS = '/downloads'
	public static SETTINGS = '/settings'
	public static FAQ = '/faq'
	public static TERMS_OF_USE = '/terms'
	public static PUBLIC_HOST_NAME = 'ytmp3.vercel.app'
	public static GITHUB = 'https://github.com/jordanshatford/youtube-to-mp3'
}

export type Route = {
	path: string
	label: string
}

export const routes: Route[] = [
	{
		label: 'Search',
		path: RoutePathConstants.SEARCH
	},
	{
		label: 'Downloads',
		path: RoutePathConstants.DOWNLOADS
	},
	{
		label: 'Settings',
		path: RoutePathConstants.SETTINGS
	}
]
