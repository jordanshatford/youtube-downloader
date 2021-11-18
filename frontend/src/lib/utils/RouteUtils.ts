export class RoutePathConstants {
	public static SEARCH = '/'
	public static DOWNLOADS = '/downloads'
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
	}
]
