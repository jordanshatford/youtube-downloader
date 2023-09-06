export class RoutePathConstants {
	public static SEARCH = '/';
	public static DOWNLOADS = '/downloads';
	public static SETTINGS = '/settings';
	public static FAQ = '/faq';
	public static TERMS_OF_USE = '/terms';
}

export type Route = {
	href: string;
	text: string;
};

export const links: Route[] = [
	{
		text: 'Search',
		href: RoutePathConstants.SEARCH
	},
	{
		text: 'Downloads',
		href: RoutePathConstants.DOWNLOADS
	},
	{
		text: 'Settings',
		href: RoutePathConstants.SETTINGS
	}
];
