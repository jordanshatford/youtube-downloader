import typescript from '@yd/config/eslint/typescript';

/** @type {import('eslint').Linter.FlatConfig} */
export default [
	...typescript,
	{
		ignores: ['dist/**/*', 'src/generated/**/*']
	}
];
