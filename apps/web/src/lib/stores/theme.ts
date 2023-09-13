import { browser } from '$app/environment';
import { writable } from 'svelte/store';

const THEME_KEY = 'theme';
const DEFAULT_THEME = 'light';

export function getInferredDefaultTheme(): 'dark' | 'light' {
	if (!window.matchMedia) {
		return DEFAULT_THEME;
	}
	if (window.matchMedia('(prefers-color-scheme: dark)').matches) {
		return 'dark';
	} else {
		return 'light';
	}
}

function createThemeStore() {
	const { subscribe, set, update } = writable<'light' | 'dark'>(DEFAULT_THEME);

	if (browser) {
		let data = localStorage?.getItem(THEME_KEY) as 'light' | 'dark';

		if (!data) {
			data = getInferredDefaultTheme();
		}
		set(data);
		if (data === 'dark') {
			document.querySelector('html')?.classList.add('dark');
		}
	}

	subscribe((value) => {
		if (browser) {
			localStorage?.setItem(THEME_KEY, value);
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
		set,
		toggle
	};
}

export const theme = createThemeStore();
