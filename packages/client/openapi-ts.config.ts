import { defineConfig } from '@hey-api/openapi-ts';
import input from '@yd/api';

export default defineConfig({
	input,
	output: './src/generated',
	client: 'fetch',
	enums: 'javascript',
	schemas: false
});
