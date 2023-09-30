import { writable, get } from 'svelte/store';
import {
	DownloadsService,
	DownloadsStatusService,
	DownloadState,
	type Video,
	type VideoWithOptionsAndStatus
} from '@yd/client';
import { toast } from '@yd/ui';
import { settings, userSettings } from '$lib/stores/settings';

export interface VideoWithExtra extends VideoWithOptionsAndStatus {
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
			updateDownload(value.id, value);
		});
	}

	async function add(video: Video) {
		if (video.id in downloads) return;

		const info: VideoWithExtra = {
			...video,
			status: { state: DownloadState.WAITING },
			options: get(settings)
		};

		updateDownload(info.id, info);
		try {
			const result = await DownloadsService.postDownloads(info);
			updateDownload(result.id, result);
		} catch (err) {
			toast.error('Error', `Failed to add '${video.title}' to downloads.`);
			console.error('Failed to add video to download ', err);
			updateDownload(info.id, { status: { state: DownloadState.ERROR } });
		}
	}

	async function restart(id: string) {
		if (!(id in downloads)) return;

		const info = downloads[id];

		updateDownload(info.id, info);
		try {
			const result = await DownloadsService.putDownloads(info);
			updateDownload(result.id, result);
		} catch (err) {
			toast.error('Error', `Failed to restart '${info.title}' download.`);
			console.error('Failed to restart download ', err);
			updateDownload(info.id, { status: { state: DownloadState.ERROR } });
		}
	}

	async function remove(id: string) {
		if (!(id in downloads)) return;

		try {
			await DownloadsService.deleteDownload(id);
			toast.success('Deleted', 'Download removed successfully.');
			update((state) => {
				delete state[id];
				return state;
			});
		} catch (err) {
			toast.error('Error', 'Failed to remove download.');
			console.error('Failed to remove download ', err);
		}
	}

	async function getFile(id: string) {
		if (!(id in downloads)) return;

		updateDownload(id, { awaitingFileBlob: true });
		try {
			const blob = await DownloadsService.getDownloadFile(id);
			const filename = `${downloads[id].title}.${downloads?.[id]?.options?.format}`;
			saveAs(blob, filename);
			updateDownload(id, { awaitingFileBlob: false });
		} catch (err) {
			toast.error('Error', 'Failed to get file for download.');
			console.error('Failed to get file for download ', err);
			updateDownload(id, { awaitingFileBlob: false, status: { state: DownloadState.ERROR } });
		}
	}

	function updateDownload(id: string, updatedValue: Partial<VideoWithExtra>) {
		update((state) => {
			const oldValue = state[id];
			const value = { ...oldValue, ...updatedValue };
			state[id] = value;
			// Automatically download file if enabled by the user.
			if (get(userSettings).autoDownloadOnComplete) {
				if (updatedValue.status?.state === DownloadState.DONE) {
					getFile(value.id);
				}
			}
			return state;
		});
	}

	return {
		subscribe,
		setupStatusListener,
		add,
		restart,
		remove,
		getFile,
		reset: () => set({})
	};
}

export const downloads = createDownloadsStore();
