import type { RouteId } from '$app/types';
import type { Component } from 'svelte';
import config, { env } from '$lib/config';

import {
	BracesIcon,
	BugIcon,
	CircleQuestionMarkIcon,
	CopyrightIcon,
	DownloadIcon,
	GitPullRequestIcon,
	HandshakeIcon,
	SearchIcon,
	SettingsIcon
} from '@yd/ui';

export const routeNamesLong: Record<RouteId, string> = {
	'/': 'Search',
	'/downloads': 'Downloads',
	'/settings': 'Settings',
	'/faq': 'Frequently Asked Questions',
	'/terms': 'Terms of Use'
};

export const routeNames: Record<RouteId, string> = {
	...routeNamesLong,
	'/faq': 'FAQ'
};

export type RouteItem = {
	title: string;
	url: RouteId | string;
	isActive?: boolean;
	icon?: Component;
	external?: boolean;
	items?: RouteItem[];
};

export const routes: { main: RouteItem[]; footer: RouteItem[] } = {
	main: [
		{
			title: routeNames['/'],
			url: '/',
			icon: SearchIcon,
			isActive: true
		},
		{
			title: routeNames['/downloads'],
			url: '/downloads',
			icon: DownloadIcon
		},
		{
			title: routeNames['/settings'],
			url: '/settings',
			icon: SettingsIcon,
			items: []
			// items: [
			// 	{
			// 		title: 'Download',
			// 		url: '/settings/downloads'
			// 	},
			// 	{
			// 		title: 'Embed',
			// 		url: '/settings/embed'
			// 	}
			// ]
		}
	],
	footer: [
		{
			title: 'API Documentation',
			url: `${env.serverAddress}/redoc`,
			icon: BracesIcon,
			external: true
		},
		{
			title: routeNames['/faq'],
			url: '/faq',
			icon: CircleQuestionMarkIcon
		},
		{
			title: routeNames['/terms'],
			url: '/terms',
			icon: HandshakeIcon
		},
		{
			title: 'Report an Issue',
			url: `${config.github}/issues/new?template=bug_report.yml`,
			icon: BugIcon,
			external: true
		},
		{
			title: 'GitHub',
			url: config.github,
			icon: GitPullRequestIcon,
			external: true
		},
		{
			title: '2021-present',
			url: `${config.github}/blob/main/LICENSE`,
			icon: CopyrightIcon,
			external: true
		}
	]
};
