export class RoutePathConstants {
	public static SEARCH = '/';
	public static DOWNLOADS = '/downloads';
	public static SETTINGS = '/settings';
	public static FAQ = '/faq';
	public static TERMS_OF_USE = '/terms';
}

export const links: { href: string; text: string }[] = [
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
