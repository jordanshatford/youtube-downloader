import { handleContextMenuClick } from '~/lib/context-menu';
import { registerContextService } from '~/lib/context-service';

export default defineBackground(() => {
	// Register service managing context of the extension.
	const contextService = registerContextService();
	// Listen for new tabs to be activated.
	browser.tabs.onActivated.addListener(async (tabInfo) => {
		if (tabInfo.tabId !== tabInfo.previousTabId) {
			const tab = await browser.tabs.get(tabInfo.tabId);
			contextService.setTab(tab);
		}
	});
	// Listen for tab updates.
	browser.tabs.onUpdated.addListener((_tabId, _tabInfo, tab) => {
		contextService.setTab(tab);
	});
	// Listen for context menu clicks.
	browser.contextMenus.onClicked.addListener((info, tab) => {
		handleContextMenuClick(info, tab);
	});
});
