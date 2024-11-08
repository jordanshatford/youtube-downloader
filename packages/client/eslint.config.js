import typescript from '@yd/config/eslint/typescript';

/** @type {import('eslint').Linter.Config} */
export default [
	{
		ignores: ['dist/**/*', 'src/generated/**/*']
	},
	...typescript
];
