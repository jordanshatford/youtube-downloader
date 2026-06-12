import adapter from '@sveltejs/adapter-auto';
import { sveltekit } from '@sveltejs/kit/vite';
import tailwindcss from '@tailwindcss/vite';
import { defineConfig } from 'vite';

import { version } from './package.json';

export default defineConfig({
	plugins: [
		tailwindcss(),
		sveltekit({
			// adapter-auto only supports some environments, see https://kit.svelte.dev/docs/adapter-auto for a list.
			// If your environment is not supported or you settled on a specific environment, switch out the adapter.
			// See https://kit.svelte.dev/docs/adapters for more information about adapters.
			adapter: adapter(),
			alias: {
				$uilib: '../../packages/ui/src/lib',
				'$uilib/*': '../../packages/ui/src/lib/*'
			}
		})
	],
	define: {
		__APP_VERSION__: JSON.stringify(version)
	}
});
