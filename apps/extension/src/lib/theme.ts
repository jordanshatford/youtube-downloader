export function initializeTheme(override?: 'dark' | 'light'): void {
	// Get preferred color scheme based on user.
	let isDark = window?.matchMedia?.('(prefers-color-scheme: dark)')?.matches;
	// Use override if provided to function.
	if (override) {
		isDark = override === 'dark';
	}
	// Add class to document so TailwindCSS knows the theme.
	if (isDark) {
		document.querySelector('html')?.classList.add('dark');
	} else {
		document.querySelector('html')?.classList.remove('dark');
	}
}
