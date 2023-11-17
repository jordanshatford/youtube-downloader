import { writable, get } from 'svelte/store';
import { Tabs } from 'webextension-polyfill';
import type { Download } from '@yd/client';
import type { Ctx } from '~/lib/context-service';
import { onMessage } from '~/lib/messaging';
import { getContextService } from '~/lib/context-service';

/**
 * Create a store used to manage context in a popup or other location. This store is initialized
 * using the context provided by the background service and will listen for any update messages
 * from the backend and maintain a reactive state for the popup. This store should be created in the
 * popup each time it is mounted. The onMount function of the store should happen in the components
 * onMount function.
 */
export function createContextStore(initial: Ctx) {
	const store = writable<Ctx & { currentDownload?: Download; tab?: Tabs.Tab }>(initial);

	// Ensure that a current download is set if one is available.
	store.update((state) => {
		state.currentDownload = state.video?.id ? state.downloads[state.video.id] : undefined;
		return state;
	});

	/**
	 * Setup all message listeners required by the store. It is important to call this in the components
	 * onMount function like `onMount(store.onMount)` as it ensures that the listeners are removed when
	 * the component is unmounted.
	 */
	function onMount(): () => void {
		browser.tabs.query({ active: true, currentWindow: true }).then((t) => {
			store.update((state) => {
				state.tab = t[0];
				return state;
			});
		});

		const cb1 = onMessage('DownloadStart', (message) => {
			store.update((state) => {
				state.downloads[message.data.video.id] = message.data;
				// If for current video update download
				if (state.video?.id === message.data.video.id) {
					state.currentDownload = message.data;
				}
				return state;
			});
		});
		const cb2 = onMessage('DownloadDone', (message) => {
			store.update((state) => {
				if (state.currentDownload?.video.id === message.data.video.id) {
					state.currentDownload = message.data;
				}
				state.downloads[message.data.video.id] = message.data;
				return state;
			});
		});
		const cb3 = onMessage('StatusUpdate', (message) => {
			store.update((state) => {
				state.downloads[message.data.video.id] = message.data;
				if (state.currentDownload?.video.id === message.data.video.id) {
					state.currentDownload = message.data;
				}
				return state;
			});
		});
		const cb4 = onMessage('VideoChanged', (message) => {
			store.update((state) => {
				if (state.tab?.url === message.data.tab.url) {
					state.video = message.data.video;
				}
				return state;
			});
		});

		return () => {
			cb1();
			cb2();
			cb3();
			cb4();
		};
	}

	async function download(): Promise<void> {
		const video = get(store).video;
		if (!video) {
			return;
		}
		const service = getContextService();
		await service.download(video);
	}

	return {
		subscribe: store.subscribe,
		onMount,
		download,
		reset: () => store.set(initial)
	};
}
