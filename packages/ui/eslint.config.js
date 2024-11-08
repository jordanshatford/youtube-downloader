import svelte from '@yd/config/eslint/svelte';

/** @type {import('eslint').Linter.Config[]} */
export default [
	{
		ignores: ['dist/', '.svelte-kit/']
	},
	...svelte
];
