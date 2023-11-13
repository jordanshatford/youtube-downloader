import config from '~/lib/config';

/**
 * Open a website in a new tab.
 * @param url - the url of the site.
 */
export async function openWebsiteURL(url: string | URL) {
	await browser.tabs.create({ url: url.toString() });
}

/**
 * Open the website for YouTube Downloader in a new tab.
 */
export async function openWebsite() {
	await openWebsiteURL(config.website);
}
