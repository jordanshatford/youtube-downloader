/** @type {import("prettier").Config} */
module.exports = {
	useTabs: true,
	singleQuote: true,
  trailingComma: "none",
  printWidth: 100,
	plugins: ["prettier-plugin-svelte", "prettier-plugin-tailwindcss"],
	overrides: [{ "files": "*.svelte", "options": { "parser": "svelte" } }]
};
