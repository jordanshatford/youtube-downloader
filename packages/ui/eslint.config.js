import svelte from '@yd/config/eslint/svelte';

/** @type {import('eslint').Linter.FlatConfig[]} */
export default [
	...svelte,
	{
		ignores: ['dist/', '.svelte-kit/']
	}
];
