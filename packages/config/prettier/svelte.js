import base from './base.js';

/** @type {import("prettier").Config} */
export default {
	...base,
	plugins: ['prettier-plugin-svelte', 'prettier-plugin-tailwindcss'],
	overrides: [{ files: '*.svelte', options: { parser: 'svelte' } }]
};
