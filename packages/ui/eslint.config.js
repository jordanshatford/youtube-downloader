import svelte from '@yd/config/eslint/svelte';

/** @type {import('eslint').Linter.FlatConfig[]} */
export default [
	{
		ignores: ['dist/', '.svelte-kit/']
	},
	...svelte
];
