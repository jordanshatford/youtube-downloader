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

	// Ensure that tab is set to the tab where the popup was opened.
	browser.tabs.query({ active: true, currentWindow: true }).then((t) => {
		store.update((state) => {
			state.tab = t[0];
			return state;
		});
	});

	/**
	 * Setup all message listeners required by the store. It is important to call this in the components
	 * onMount function like `onMount(store.onMount)` as it ensures that the listeners are removed when
	 * the component is unmounted.
	 */
	function onMount(): () => void {
		const cb1 = onMessage('VideoChanged', (message) => {
			store.update((state) => {
				// Ignore any VideoChanges for tabs aside from this tab.
				if (state.tab?.url === message.data.tab.url) {
					state.video = message.data.video;
				}
				return state;
			});
		});
		const cb2 = onMessage('DownloadStart', (message) => {
			handleUpdate(message.data);
		});
		const cb3 = onMessage('StatusUpdate', (message) => {
			handleUpdate(message.data);
		});
		const cb4 = onMessage('DownloadDone', (message) => {
			handleUpdate(message.data);
		});
		const cb5 = onMessage('DownloadRemove', (message) => {
			store.update((state) => {
				if (message.data in state.downloads) {
					delete state.downloads[message.data];
				}
				if (state.currentDownload?.video.id === message.data) {
					state.currentDownload = undefined;
				}
				return state;
			});
		});
		return () => {
			cb1();
			cb2();
			cb3();
			cb4();
			cb5();
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

	async function getFile(id: string): Promise<void> {
		const service = getContextService();
		await service.getFile(id);
	}

	async function remove(id: string): Promise<void> {
		const service = getContextService();
		await service.remove(id);
	}

	async function restart(id: string) {
		const service = getContextService();
		await service.restart(id);
	}

	async function handleUpdate(download: Download) {
		store.update((state) => {
			// Update the downloads map with new value.
			state.downloads[download.video.id] = download;
			// If the update is for this tabs video, update the current download.
			if (state.video?.id === download.video.id) {
				state.currentDownload = download;
			}
			return state;
		});
	}

	return {
		subscribe: store.subscribe,
		onMount,
		download,
		getFile,
		remove,
		restart,
		reset: () => store.set(initial)
	};
}
