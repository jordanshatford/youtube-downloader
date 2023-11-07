import { defineConfig } from 'wxt';
import { svelte, vitePreprocess } from '@sveltejs/vite-plugin-svelte';

// See https://wxt.dev/api/config.html
export default defineConfig({
	srcDir: 'src',
	manifest: {
		name: 'YouTube Downloader',
		permissions: ['contextMenus', 'tabs']
	},
	vite: () => ({
		plugins: [
			svelte({
				// Using a svelte.config.js file causes a segmentation fault when importing the file
				configFile: false,
				preprocess: [vitePreprocess()]
			})
		]
	})
});
