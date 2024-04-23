import type { Menus, Tabs } from 'webextension-polyfill';

import type { Video } from '@yd/client';

import { getContextService } from './context-service';

export function handleContextMenuClick(info: Menus.OnClickData, tab?: Tabs.Tab): void {
	if (!tab || !tab.url) {
		return;
	}

	if (info.menuItemId === 'yd-download') {
		const service = getContextService();
		service.downloadURL(tab.url);
	}
}

export async function setContextMenus(video?: Video): Promise<void> {
	// Remove exisiting context menu.
	await browser.contextMenus.removeAll();

	// If there is no current video, dont add context menu.
	if (!video) {
		return;
	}

	// Add in new context menu.
	const mainMenuID = 'youtube-download-main-context-menu';
	// Main context menu.
	browser.contextMenus.create({
		id: mainMenuID,
		title: 'YouTube Downloader',
		contexts: ['all']
	});

	// Submenu options for the context menu
	const submenus: Partial<Menus.CreateCreatePropertiesType>[] = [
		{
			id: 'yd-download',
			title: `Download '${video.title}'`
		}
	];

	for (const menu of submenus) {
		browser.contextMenus.create({
			...menu,
			parentId: mainMenuID,
			contexts: ['all']
		});
	}
}
