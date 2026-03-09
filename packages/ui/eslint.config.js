import { defineConfig } from 'eslint/config';

import svelte from '@yd/config/eslint/svelte';

export default defineConfig([
	{
		ignores: ['dist/', '.svelte-kit/']
	},
	...svelte
]);
