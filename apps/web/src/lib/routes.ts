import type { RouteId } from '$app/types';

import type { IconSource } from '@yd/ui';
import { DownloadIcon, GearIcon, MagnifyingGlassIcon } from '@yd/ui';

export class RoutePathConstants {
	public static SEARCH: RouteId = '/';
	public static DOWNLOADS: RouteId = '/downloads';
	public static SETTINGS: RouteId = '/settings';
	public static FAQ: RouteId = '/faq';
	public static TERMS_OF_USE: RouteId = '/terms';
}

export const navbarLinks: { href: RouteId; text: string; icon?: IconSource }[] = [
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

export const footerLinks: { href: RouteId; text: string }[] = [
	{
		href: RoutePathConstants.FAQ,
		text: 'faq'
	},
	{
		href: RoutePathConstants.TERMS_OF_USE,
		text: 'terms of use'
	}
];
