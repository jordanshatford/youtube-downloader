import { download, search } from '$lib/components/icons'

export class RoutePathConstants {
	public static SEARCH = '/'
	public static DOWNLOADS = '/downloads'
}

export type Route = {
	path: string
	label: string
	icon: string
}

export const routes = [
	{
		label: 'Search',
		path: RoutePathConstants.SEARCH,
		icon: search
	},
	{
		label: 'Downloads',
		path: RoutePathConstants.DOWNLOADS,
		icon: download
	}
]
