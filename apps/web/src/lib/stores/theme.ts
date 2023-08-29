import { browser } from '$app/environment';
import { writable } from 'svelte/store';

const THEME_KEY = 'theme';

function createThemeStore() {
	const { subscribe, set, update } = writable<'light' | 'dark'>('light');

	if (browser) {
		const data = localStorage?.getItem(THEME_KEY) as 'light' | 'dark';

		if (data) {
			set(data);
			if (data === 'dark') {
				document.querySelector('html')?.classList.add('dark');
			}
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
