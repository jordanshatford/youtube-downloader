import eslintPluginSvelte from 'eslint-plugin-svelte';
import globals from 'globals';
import svelte from 'svelte-eslint-parser';
import tseslint from 'typescript-eslint';

import eslintTypeScript from './typescript.js';

/** @type {import('eslint').Linter.Config[]} */
export default tseslint.config(
	...eslintTypeScript,
	...eslintPluginSvelte.configs['flat/recommended'],
	{
		languageOptions: {
			parserOptions: {
				extraFileExtensions: ['**/*.svelte']
			}
		}
	},
	{
		files: ['**/*.svelte'],
		languageOptions: {
			parser: svelte,
			parserOptions: {
				parser: tseslint.parser
			}
		}
	}
);

export const webextensions = globals.webextensions;
