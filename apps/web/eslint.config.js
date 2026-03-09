import { defineConfig } from 'eslint/config';

import svelte from '@yd/config/eslint/svelte';

export default defineConfig([
	{
		ignores: ['build/', '.svelte-kit/']
	},
	...svelte
]);
