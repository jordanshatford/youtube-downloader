/** @type {import('@nicolas-chaulet/openapi-typescript-codegen').UserConfig} */
module.exports = {
	input: require('@yd/api'),
	output: './src/generated',
	client: 'fetch',
	enums: true,
	exportSchemas: false
};
