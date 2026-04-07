import type { RouteId } from '$app/types';
import type { Component } from 'svelte';
import config, { env } from '$lib/config';

import {
	BracesIcon,
	BugIcon,
	CircleQuestionMarkIcon,
	CodeIcon,
	CopyrightIcon,
	DownloadIcon,
	GitPullRequestIcon,
	HandshakeIcon,
	SearchIcon,
	SettingsIcon
} from '@yd/ui';

export type RouteItem = {
	title: string;
	titleLong?: string;
	url: RouteId | string;
	isActive?: boolean;
	icon?: Component;
	external?: boolean;
	items?: RouteItem[];
};

export const settingsRoutes: RouteItem[] = [
	{
		title: 'Download',
		url: '/settings/download',
		icon: DownloadIcon
	},
	{
		title: 'Embed',
		url: '/settings/embed',
		icon: CodeIcon
	}
];

export const routes: { main: RouteItem[]; footer: RouteItem[] } = {
	main: [
		{
			title: 'Search',
			url: '/',
			icon: SearchIcon,
			isActive: true
		},
		{
			title: 'Downloads',
			url: '/downloads',
			icon: DownloadIcon
		},
		{
			title: 'Settings',
			url: '/settings',
			icon: SettingsIcon,
			items: settingsRoutes
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
			title: 'FAQ',
			titleLong: 'Frequently Asked Questions',
			url: '/faq',
			icon: CircleQuestionMarkIcon
		},
		{
			title: 'Terms of Use',
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
