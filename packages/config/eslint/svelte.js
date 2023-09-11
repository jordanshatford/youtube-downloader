/** @type {import('eslint').Linter.Config} */
module.exports = {
	extends: [
    require.resolve('./typescript.js'),
		'plugin:svelte/recommended',
	],
	parserOptions: {
		extraFileExtensions: ['.svelte']
	},
	overrides: [
		{
			files: ['*.svelte'],
			parser: 'svelte-eslint-parser',
			parserOptions: {
				parser: '@typescript-eslint/parser'
			}
		}
	]
};
