import { defineConfig } from '@hey-api/openapi-ts';

export default defineConfig({
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
      name: '@hey-api/client-fetch',
    },
		{
			name: '@hey-api/sdk'
		}
	]
});
