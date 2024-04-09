import typescript from '@yd/config/eslint/typescript';

/** @type {import('eslint').Linter.FlatConfig} */
export default [
	{
		ignores: ['dist/**/*', 'src/generated/**/*']
	},
	...typescript
];
