import { defineConfig } from '@hey-api/openapi-ts';

import input from '@yd/api';

export default defineConfig({
	client: 'fetch',
	input,
	output: {
		format: 'prettier',
		path: './src/generated'
	},
	schemas: false,
	services: {
		asClass: true
	},
	types: {
		enums: 'javascript'
	}
});
