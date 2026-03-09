import { defineConfig } from 'eslint/config';

import typescript from '@yd/config/eslint/typescript';

export default defineConfig([
	{
		ignores: ['dist/**/*', 'src/generated/**/*']
	},
	...typescript
]);
