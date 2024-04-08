import globals from 'globals';
import tseslint from 'typescript-eslint';
import eslintPluginSvelte from 'eslint-plugin-svelte';
import eslintTypeScript from './typescript.js';
import svelte from 'svelte-eslint-parser';

/** @type {import('eslint').Linter.FlatConfig[]} */
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
