export default defineBackground(() => {
	// Listen for new tabs to be activated.
	browser.tabs.onActivated.addListener(async (tabInfo) => {
		if (tabInfo.tabId !== tabInfo.previousTabId) {
			const tab = await browser.tabs.get(tabInfo.tabId);
			console.info(tab);
		}
	});
	// Listen for tab updates.
	browser.tabs.onUpdated.addListener((_tabId, _tabInfo, tab) => {
		console.info(tab);
	});
});
