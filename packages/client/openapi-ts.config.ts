import { defineConfig } from '@hey-api/openapi-ts';

import input from '@yd/api';

export default defineConfig({
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
			name: '@hey-api/client-fetch'
		},
		{
			name: '@hey-api/sdk'
		}
	]
});
