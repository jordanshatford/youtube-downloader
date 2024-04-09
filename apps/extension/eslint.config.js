import svelte, { webextensions } from '@yd/config/eslint/svelte';

/** @type {import('eslint').Linter.FlatConfig[]} */
export default [
	{
		ignores: ['.wxt/', '.output/']
	},
	...svelte,
	{
		languageOptions: {
			globals: {
				...webextensions
			}
		}
	}
];
