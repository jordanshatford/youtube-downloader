import svelte, { webextensions } from '@yd/config/eslint/svelte';

/** @type {import('eslint').Linter.Config[]} */
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
