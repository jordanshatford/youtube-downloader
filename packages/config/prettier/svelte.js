import svelte from 'prettier-plugin-svelte';

import base from './base.js';

/** @type {import("prettier").Config} */
export default {
	...base,
	plugins: [...base.plugins, svelte, 'prettier-plugin-tailwindcss'],
	overrides: [{ files: '*.svelte', options: { parser: 'svelte' } }]
};
