import { defineConfig } from "@hey-api/openapi-ts";
// @ts-ignore
import input from '@yd/api';

export default defineConfig({
	input,
	output: './src/generated',
	client: 'fetch',
	enums: 'javascript',
	exportSchemas: false
});
