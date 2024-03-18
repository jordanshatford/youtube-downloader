/** @type {import('@nicolas-chaulet/openapi-typescript-codegen').Config} */
module.exports = {
	input: require('@yd/api'),
	output: './src/generated',
	client: 'fetch',
	enums: true
};
