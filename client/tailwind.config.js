const colors = require('tailwindcss/colors')

module.exports = {
  purge: {
    // enabled: true,
    content: ['./src/**/*.svelte'],
  },
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
      },
    },
  },
  variants: {
    extend: {
      backgroundColor: ['active', 'responsive', 'disabled', 'dark', 'group-hover', 'focus-within', 'hover', 'focus'],
      cursor: ['responsive', 'disabled'],
      divideColor: ['responsive', 'dark'],
      opacity: ['responsive', 'group-hover', 'focus-within', 'hover', 'focus', 'disabled'],
      scale: ['responsive', 'hover', 'focus'],
      textColor: ['responsive', 'dark', 'group-hover', 'focus-within', 'hover', 'focus', 'disabled'],
    }
  },
  plugins: [],
}