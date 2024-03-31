/** @type {import('@hey-api/openapi-ts').UserConfig} */
module.exports = {
	input: require('@yd/api'),
	output: './src/generated',
	client: 'fetch',
	enums: 'javascript',
	exportSchemas: false
};
