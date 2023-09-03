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
import { toast } from '$lib/components/ui/toast';

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

	async function add(video: Video) {
		if (video.id in downloads) return;

		const info: VideoWithExtra = {
			...video,
			state: DownloadState.WAITING,
			options: {
				format: get(settings).format ?? AudioFormat.MP3
			}
		};

		update((state) => Object.assign(state, { [info.id]: info }));
		try {
			const result = await DownloadsService.postDownloads(info);
			toast.info(`Added '${video.title}' to downloads.`);
			update((state) => Object.assign(state, { [result.id]: result }));
		} catch (err) {
			toast.error(`Failed to add '${video.title}' to downloads.`);
			console.error('Failed to add video to download ', err);
			update((state) => {
				state[info.id].state = DownloadState.ERROR;
				return state;
			});
		}
	}

	async function remove(id: string) {
		if (!(id in downloads)) return;

		try {
			await DownloadsService.deleteDownload(id);
			toast.success('Download removed successfully.');
			update((state) => {
				delete state[id];
				return state;
			});
		} catch (err) {
			toast.error('Failed to remove download.');
			console.error('Failed to remove download ', err);
		}
	}

	async function getFile(id: string) {
		if (!(id in downloads)) return;

		update((state) => {
			state[id].awaitingFileBlob = true;
			return state;
		});
		try {
			const blob = await DownloadsService.getDownloadFile(id);
			const filename = `${downloads[id].title}.${downloads?.[id]?.options?.format}`;
			saveAs(blob, filename);
			update((state) => {
				state[id].awaitingFileBlob = false;
				return state;
			});
		} catch {
			toast.error('Failed to get file for download.');
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
