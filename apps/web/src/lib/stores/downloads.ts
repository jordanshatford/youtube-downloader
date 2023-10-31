import { writable, get } from 'svelte/store';
import {
	DownloadsService,
	DownloadsStatusService,
	DownloadState,
	type Video,
	type Download
} from '@yd/client';
import { toast } from '@yd/ui';
import { settings, userSettings } from '$lib/stores/settings';
import { saveAs } from '$lib/utils/files';

export interface DownloadWithExtra extends Download {
	awaitingFileBlob?: boolean;
}

function createDownloadsStore() {
	const downloads: Record<string, DownloadWithExtra> = {};

	const { subscribe, set, update } = writable(downloads);

	function setupStatusListener() {
		DownloadsStatusService.setup((download) => {
			updateDownload(download.video.id, download);
		});
	}

	async function add(video: Video) {
		if (video.id in downloads) return;

		const download: DownloadWithExtra = {
			video,
			status: { state: DownloadState.WAITING, progress: null },
			options: get(settings)
		};

		// Add initial value for the download
		update((state) => {
			state[download.video.id] = download;
			return state;
		});

		try {
			const result = await DownloadsService.postDownloads(download);
			updateDownload(result.video.id, result);
		} catch (err) {
			handleError(download.video.id, `Failed to add '${video.title}' to downloads.`, err);
		}
	}

	async function restart(id: string) {
		if (!(id in downloads)) return;

		const download = downloads[id];

		try {
			const result = await DownloadsService.putDownloads(download);
			updateDownload(result.video.id, result);
		} catch (err) {
			handleError(download.video.id, `Failed to restart '${download.video.title}' download.`, err);
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
			handleError(id, 'Failed to remove download.', err);
		}
	}

	async function getFile(id: string) {
		if (!(id in downloads)) return;

		updateDownload(id, { awaitingFileBlob: true });
		try {
			const blob = await DownloadsService.getDownloadFile(id);
			const filename = `${downloads[id].video.title}.${downloads?.[id]?.options?.format}`;
			saveAs(blob, filename);
		} catch (err) {
			handleError(id, 'Failed to get file for download.', err);
		} finally {
			updateDownload(id, { awaitingFileBlob: false });
		}
	}

	function handleError(downloadId: string, msg: string, error: unknown) {
		toast.error('Error', msg);
		console.error(msg, error);
		updateDownload(downloadId, { status: { state: DownloadState.ERROR, progress: null } });
	}

	function updateDownload(id: string, updatedValue: Partial<DownloadWithExtra>) {
		update((state) => {
			if (id in state) {
				// Merge and update values.
				const oldValue = state[id];
				const value: DownloadWithExtra = { ...oldValue, ...updatedValue };
				state[id] = value;
				// Automatically download file if enabled by the user.
				if (get(userSettings).autoDownloadOnComplete) {
					if (updatedValue.status?.state === DownloadState.DONE) {
						getFile(value.video.id);
					}
				}
			} else {
				console.error('ID NOT IN STATE');
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
