import type { SvelteComponent } from 'svelte'
import { DownloadIcon, SearchIcon } from 'svelte-feather-icons'

export class RoutePathConstants {
	public static SEARCH = '/'
	public static DOWNLOADS = '/downloads'
}

export type Route = {
	path: string
	label: string
	icon: typeof SvelteComponent
}

export const routes: Route[] = [
	{
		label: 'Search',
		path: RoutePathConstants.SEARCH,
		icon: SearchIcon
	},
	{
		label: 'Downloads',
		path: RoutePathConstants.DOWNLOADS,
		icon: DownloadIcon
	}
]
