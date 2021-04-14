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
  variants: {},
  plugins: [],
}