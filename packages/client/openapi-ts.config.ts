import { defineConfig } from '@hey-api/openapi-ts';

import input from '@yd/api';

export default defineConfig({
	client: '@hey-api/client-fetch',
	input,
	output: {
		format: 'prettier',
		path: './src/generated'
	},
	plugins: [
		{
			name: '@hey-api/typescript',
			enums: 'javascript'
		},
		{
			name: '@hey-api/sdk'
		}
	]
});
