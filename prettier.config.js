/**
 * @see https://prettier.io/docs/configuration
 * @type {import("prettier").Config & import("@ianvs/prettier-plugin-sort-imports").PluginConfig}
 */
export default {
	useTabs: true,
	singleQuote: true,
	trailingComma: 'none',
	printWidth: 100,
	plugins: [
		'@prettier/plugin-oxc',
		'@ianvs/prettier-plugin-sort-imports',
		'prettier-plugin-svelte',
		'prettier-plugin-tailwindcss'
	],
	importOrder: [
		'<TYPES>^(node:)',
		'<BUILT_IN_MODULES>',
		'',
		'<TYPES>',
		'<THIRD_PARTY_MODULES>',
		'',
		'<TYPES>^@yd/(.*)$',
		'^@yd/(.*)$',
		'',
		'<TYPES>^$app/(.*)$',
		'^$app/(.*)$',
		'<TYPES>^$lib/(.*)$',
		'^$lib/(.*)$',
		'<TYPES>^~(.*)$',
		'^~(.*)$',
		'<TYPES>^~/(.*)$',
		'^~/(.*)$',
		'<TYPES>^@/(.*)$',
		'^@/(.*)$',
		'<TYPES>^[.]',
		'^[.]'
	],
	importOrderTypeScriptVersion: '5.0.0',
	overrides: [{ files: '*.svelte', options: { parser: 'svelte' } }]
};
