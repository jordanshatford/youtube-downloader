/** @type {import("prettier").Config} */
module.exports = {
	...require('./base'),
	plugins: ['prettier-plugin-svelte', 'prettier-plugin-tailwindcss'],
	overrides: [{ files: '*.svelte', options: { parser: 'svelte' } }]
};
