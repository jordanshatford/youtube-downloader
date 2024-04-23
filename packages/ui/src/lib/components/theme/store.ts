import { writable } from 'svelte/store';

import { browser } from '../../utilities';

type Theme = 'dark' | 'light';

const THEME_LOCALSTORAGE_KEY = 'theme';
const DEFAULT_THEME: Theme = 'light';

// Get the default theme value inferred by the browser settings.
function getInferredDefaultTheme(): Theme {
	if (browser()) {
		// Cant match preferred color scheme, return default.
		if (!window.matchMedia) {
			return DEFAULT_THEME;
		}
		// Use dark theme if preferred by the user.
		if (window.matchMedia('(prefers-color-scheme: dark)').matches) {
			return 'dark';
		} else {
			return 'light';
		}
	} else {
		return DEFAULT_THEME;
	}
}

// Initialize document with a given theme. Tailwind will handle styling dark or light.
export function initializeTheme(override?: Theme): Theme {
	const theme = override ? override : getInferredDefaultTheme();
	if (theme === 'dark') {
		document.querySelector('html')?.classList.add('dark');
	} else {
		document.querySelector('html')?.classList.remove('dark');
	}
	return theme;
}

function createThemeStore() {
	const { subscribe, set, update } = writable<Theme>(getInferredDefaultTheme());

	if (browser()) {
		const data = localStorage?.getItem(THEME_LOCALSTORAGE_KEY) as Theme;
		const theme = initializeTheme(data);
		set(theme);
	}

	subscribe((value) => {
		if (browser()) {
			localStorage?.setItem(THEME_LOCALSTORAGE_KEY, value);
		}
	});

	function toggle() {
		update((state) => {
			state = state === 'dark' ? 'light' : 'dark';
			return state;
		});
		document.querySelector('html')?.classList.toggle('dark');
	}

	return {
		subscribe,
		toggle
	};
}

export const theme = createThemeStore();
