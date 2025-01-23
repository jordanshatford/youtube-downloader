import importsort from '@ianvs/prettier-plugin-sort-imports';

/** @type {import("prettier").Config} */
export default {
	useTabs: true,
	singleQuote: true,
	trailingComma: 'none',
	printWidth: 100,
	plugins: [importsort],
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
	importOrderTypeScriptVersion: '5.0.0'
};
