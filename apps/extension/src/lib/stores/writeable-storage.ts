import { writable, get, type Updater, type Writable } from 'svelte/store';
import { Storage } from 'webextension-polyfill';

export interface WriteableStorage<T> extends Writable<T> {
	initialize(): Promise<void>;
	set(value: T): Promise<void>;
	update(updater: Updater<T>): Promise<void>;
}

// Create a Svelte store wrapping browser extension storage. This should always be initialized
// using the initialize method before attempting to use it. By default sync storage is used,
// unless specified otherwise by the user.
export function writeableStorage<T>(
	key: string,
	initial?: T,
	storage: Storage.StorageArea = browser.storage.sync
) {
	const store = writable(initial);

	// Wrap set function in async to support storage.
	async function set(value: T) {
		await storage.set({ [key]: value });
		store.set(value);
	}

	// Wrap update function in async to support storage.
	async function update(updater: Updater<T>) {
		const value = updater(get(store));
		await set(value);
	}

	// Initialize the store with values from storage.
	async function initialize() {
		const result = await storage.get(key);
		const value: T = result?.[key] || initial;
		await set(value);
	}

	return {
		initialize,
		// Return similiar interface as regular Svelte store (but async)
		subscribe: store.subscribe,
		set,
		update
	};
}
