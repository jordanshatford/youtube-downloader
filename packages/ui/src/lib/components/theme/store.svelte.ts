import { browser } from '../../utilities';

type Theme = 'dark' | 'light';

const THEME_LOCALSTORAGE_KEY = 'theme';
const DEFAULT_THEME: Theme = 'light';

// Get the default theme value inferred by the browser settings.
function getInferredDefaultTheme(fallback: Theme): Theme {
	if (browser()) {
		// Cant match preferred color scheme, return default.
		if (!window.matchMedia) {
			return fallback;
		}
		// Use dark theme if preferred by the user.
		if (window.matchMedia('(prefers-color-scheme: dark)').matches) {
			return 'dark';
		} else {
			return 'light';
		}
	} else {
		return fallback;
	}
}

class ThemeStore {
	private theme = $state<Theme>(getInferredDefaultTheme(DEFAULT_THEME));
	public isDark = $derived(this.theme === 'dark');

	public constructor() {
		if (browser()) {
			const data = localStorage?.getItem(THEME_LOCALSTORAGE_KEY) as Theme;
			const theme = data ? data : getInferredDefaultTheme(DEFAULT_THEME);
			if (theme === 'dark') {
				document.querySelector('html')?.classList.add('dark');
			} else {
				document.querySelector('html')?.classList.remove('dark');
			}
			this.theme = theme;
		}
	}

	public toggle() {
		this.theme = this.theme === 'dark' ? 'light' : 'dark';
		document.querySelector('html')?.classList.toggle('dark');
		if (browser()) {
			localStorage?.setItem(THEME_LOCALSTORAGE_KEY, this.theme);
		}
	}
}

export const theme = new ThemeStore();
