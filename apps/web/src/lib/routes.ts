import type { IconSource } from '@yd/ui';
import { DownloadIcon, GearIcon, MagnifyingGlassIcon } from '@yd/ui';

export class RoutePathConstants {
	public static SEARCH = '/';
	public static DOWNLOADS = '/downloads';
	public static SETTINGS = '/settings';
	public static FAQ = '/faq';
	public static TERMS_OF_USE = '/terms';
}

export const navbarLinks: { href: string; text: string; icon?: IconSource }[] = [
	{
		text: 'Search',
		href: RoutePathConstants.SEARCH,
		icon: MagnifyingGlassIcon
	},
	{
		text: 'Downloads',
		href: RoutePathConstants.DOWNLOADS,
		icon: DownloadIcon
	},
	{
		text: 'Settings',
		href: RoutePathConstants.SETTINGS,
		icon: GearIcon
	}
];

export const footerLinks: { href: string; text: string }[] = [
	{
		href: RoutePathConstants.FAQ,
		text: 'faq'
	},
	{
		href: RoutePathConstants.TERMS_OF_USE,
		text: 'terms of use'
	}
];
