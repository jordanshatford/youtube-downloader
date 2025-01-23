import { defineConfig } from '@hey-api/openapi-ts';

export default defineConfig({
	client: '@hey-api/client-fetch',
	input: '../../apps/api/openapi.json',
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
