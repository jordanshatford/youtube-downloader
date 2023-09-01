import { writable, get } from 'svelte/store';
import {
	DownloadsService,
	DownloadsStatusService,
	DownloadState,
	AudioFormat,
	type Video,
	type VideoWithOptions
} from '@yd/client';
import { settings } from '$lib/stores/settings';

interface VideoWithExtra extends VideoWithOptions {
	state: DownloadState;
	awaitingFileBlob?: boolean;
}

function saveAs(blob: Blob, name: string) {
	// Create anchor tag referencing the blob
	const url = window.URL.createObjectURL(blob);
	const a = document.createElement('a');
	a.href = url;
	a.download = name;
	// Append anchor and click to download
	document.body.appendChild(a);
	a.click();
	// Cleanup
	a.remove();
}

function createDownloadsStore() {
	const downloads: Record<string, VideoWithExtra> = {};

	const { subscribe, set, update } = writable(downloads);

	function setupStatusListener() {
		DownloadsStatusService.setup((value) => {
			update((state) => {
				state[value.id].state = value.state;
				return state;
			});
		});
	}

	function add(video: Video) {
		if (video.id in downloads) return;

		const info: VideoWithExtra = {
			...video,
			state: DownloadState.WAITING,
			options: {
				format: get(settings).format ?? AudioFormat.MP3
			}
		};

		// Add download to store using information we have already
		update((state) => Object.assign(state, { [info.id]: info }));
		try {
			DownloadsService.postDownloads(info);
		} catch (err) {
			console.error('Failed to add video to download ', err);
			update((state) => {
				state[info.id].state = DownloadState.ERROR;
				return state;
			});
		}
	}

	function remove(id: string) {
		if (!(id in downloads)) return;

		update((state) => {
			delete state[id];
			return state;
		});
		DownloadsService.deleteDownload(id);
	}

	async function getFile(id: string) {
		if (!(id in downloads)) return;

		update((state) => {
			state[id].awaitingFileBlob = true;
			return state;
		});
		try {
			const blob = await DownloadsService.getDownloadFile(id);
			update((state) => {
				state[id].awaitingFileBlob = false;
				return state;
			});
			const filename = `${downloads[id].title}.${downloads?.[id]?.options?.format}`;
			saveAs(blob, filename);
		} catch {
			remove(id);
		}
	}

	return {
		subscribe,
		setupStatusListener,
		add,
		remove,
		getFile,
		reset: () => set({})
	};
}

export const downloads = createDownloadsStore();
