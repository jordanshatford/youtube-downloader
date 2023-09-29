import colors from 'tailwindcss/colors';

/** @type {import('tailwindcss').Config} */
export default {
	content: [
		'./src/**/*.{html,js,svelte,ts}',
		'../../apps/*/src/**/*.{html,js,svelte,ts}',
		'../../packages/*/src/**/*.{html,js,svelte,ts}'
	],
	darkMode: 'class',
	theme: {
		extend: {
			boxShadow: {
				dark: '0px 2px 4px 0px hsla(0,0%,0%,0.14), 0px 2px 4px 0px hsla(0,0%,0%,0.12), 0px 2px 4px -1px hsla(0,0%,0%,0.2);'
			},
			colors: {
				brand: colors.blue
			}
		}
	},
	variants: {
		extend: {
			backgroundColor: [
				'active',
				'responsive',
				'disabled',
				'dark',
				'group-hover',
				'focus-within',
				'hover',
				'focus'
			],
			boxShadow: ['dark', 'responsive', 'group-hover', 'focus-within', 'hover', 'focus'],
			cursor: ['responsive', 'disabled'],
			divideColor: ['responsive', 'dark'],
			opacity: ['responsive', 'group-hover', 'focus-within', 'hover', 'focus', 'disabled'],
			scale: ['responsive', 'hover', 'focus'],
			textColor: ['responsive', 'dark', 'group-hover', 'focus-within', 'hover', 'focus', 'disabled']
		}
	},
	plugins: [require('@tailwindcss/forms')]
};
