const colors = require('tailwindcss/colors')

module.exports = {
  purge: {
    enabled: true,
    content: ['./src/**/*.svelte'],
  },
  theme: {
    extend: {
      colors: {
      },
    },
  },
  variants: {
    extend: {
      cursor: ['responsive', 'disabled'],
      opacity: ['responsive', 'group-hover', 'focus-within', 'hover', 'focus', 'disabled'],
      textColor: ['responsive', 'dark', 'group-hover', 'focus-within', 'hover', 'focus', 'disabled'],
    }
  },
  plugins: [],
}