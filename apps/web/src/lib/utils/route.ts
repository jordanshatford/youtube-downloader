export class RoutePathConstants {
	public static SEARCH = '/';
	public static DOWNLOADS = '/downloads';
	public static SETTINGS = '/settings';
	public static FAQ = '/faq';
	public static TERMS_OF_USE = '/terms';
}

export type Route = {
	path: string;
	label: string;
};

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
];
