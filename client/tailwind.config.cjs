const config = {
	purge: ['./src/**/*.{html,js,svelte,ts}'],
	darkMode: 'class',
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
			cursor: ['responsive', 'disabled'],
			divideColor: ['responsive', 'dark'],
			opacity: ['responsive', 'group-hover', 'focus-within', 'hover', 'focus', 'disabled'],
			scale: ['responsive', 'hover', 'focus'],
			textColor: ['responsive', 'dark', 'group-hover', 'focus-within', 'hover', 'focus', 'disabled']
		}
	},
	plugins: []
}

module.exports = config
