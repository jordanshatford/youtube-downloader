import svelte from '@yd/config/eslint/svelte';

/** @type {import('eslint').Linter.FlatConfig[]} */
export default [
	{
		ignores: ['build/', '.svelte-kit/']
	},
	...svelte
];
