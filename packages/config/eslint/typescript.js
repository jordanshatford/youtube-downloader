import eslint from '@eslint/js';
import prettier from 'eslint-config-prettier';
import { defineConfig } from 'eslint/config';
import globals from 'globals';
import tseslint from 'typescript-eslint';

export default defineConfig([
	{
		ignores: [
			'.DS_Store',
			'node_modules/*',
			'.env',
			'.env.*',
			'!.env.sample',
			'pnpm-lock.yaml',
			'package-lock.json',
			'yarn.lock'
		]
	},
	eslint.configs.recommended,
	...tseslint.configs.recommended,
	prettier,
	{
		languageOptions: {
			globals: {
				...globals.browser,
				...globals.es2017,
				...globals.node
			},
			parserOptions: {
				sourceType: 'module',
				ecmaVersion: 2020
			}
		}
	}
]);
