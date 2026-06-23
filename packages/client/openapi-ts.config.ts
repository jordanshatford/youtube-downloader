import { defineConfig, plugins } from '@hey-api/openapi-ts';

import input from '@yd/api';

export default defineConfig({
	input,
	output: {
		postProcess: ['prettier'],
		path: './src/generated'
	},
	plugins: [
		plugins.typescript({
			enums: 'javascript'
		}),
		plugins.sdk(),
		plugins.clientFetch()
	]
});
