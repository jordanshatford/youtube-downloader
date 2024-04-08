import svelte, { webextensions } from '@yd/config/eslint/svelte';

/** @type {import('eslint').Linter.FlatConfig[]} */
export default [
	...svelte,
	{
		languageOptions: {
			globals: {
				...webextensions
			}
		},
		ignores: ['.wxt/', '.output/']
	}
];
