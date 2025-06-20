import { SESSION_ID_KEY } from '$lib/api';
import { settings, userSettings } from '$lib/stores/settings.svelte';
import { saveAs } from '$lib/utils/files';

import type { Download, Video } from '@yd/client';
import {
	deleteDownload,
	getDownloadFile,
	getDownloads,
	getDownloadsStatus,
	postDownloads,
	putDownloads
} from '@yd/client';
import { toasts } from '@yd/ui';

class DownloadsStore {
	public downloads = $state<Record<string, Download>>({});

	public async init() {
		// Setup listener for status updates of any downloads.
		getDownloadsStatus(() => localStorage.getItem(SESSION_ID_KEY) ?? '', {
			onMessage: (download) => {
				this.updateDownload(download.video.id, download);
			}
		});
		// Get all previous downloads still available.
		const { data: downloads } = await getDownloads();
		if (downloads) {
			this.downloads = downloads.reduce((prev, curr) => ({ ...prev, [curr.video.id]: curr }), {});
		} else {
			this.downloads = {};
		}
	}

	public async add(video: Video) {
		if (video.id in this.downloads) return;

		const download: Download = {
			video,
			status: { state: 'WAITING', progress: null },
			options: settings.settings
		};

		// Add initial value for the download
		this.downloads[download.video.id] = download;

		try {
			const { data: result } = await postDownloads({
				body: download
			});
			if (result) {
				this.updateDownload(result.video.id, result);
			}
		} catch (err) {
			this.handleError(download.video.id, `Failed to add '${video.title}' to downloads.`, err);
		}
	}

	public async restart(id: string) {
		if (!(id in this.downloads)) return;

		const download = this.downloads[id];

		try {
			const { data: result } = await putDownloads({
				body: download
			});
			if (result) {
				this.updateDownload(result.video.id, result);
			}
		} catch (err) {
			this.handleError(
				download.video.id,
				`Failed to restart '${download.video.title}' download.`,
				err
			);
		}
	}

	public async remove(id: string) {
		if (!(id in this.downloads)) return;

		try {
			await deleteDownload({ path: { download_id: id } });
			toasts.success('Deleted', 'Download removed successfully.');
			delete this.downloads[id];
		} catch (err) {
			this.handleError(id, 'Failed to remove download.', err);
		}
	}

	public async getFile(id: string) {
		if (!(id in this.downloads)) return;

		try {
			const { data: file } = await getDownloadFile({
				path: { download_id: id }
			});
			if (file) {
				const download = this.downloads[id];
				const filename = `${download.video.title}.${download.options.format}`;
				saveAs(file as Blob, filename);
			}
		} catch (err) {
			this.handleError(id, 'Failed to get file for download.', err);
		}
	}

	private updateDownload(id: string, updatedValue: Partial<Download>) {
		if (id in this.downloads) {
			// Merge and update values.
			const oldValue = this.downloads[id];
			const value: Download = { ...oldValue, ...updatedValue };
			this.downloads[id] = value;
			// Automatically download file if enabled by the user.
			if (userSettings.settings.autoDownloadOnComplete) {
				if (updatedValue.status?.state === 'DONE') {
					this.getFile(value.video.id);
				}
			}
		} else {
			console.error('Attempted to update download that does not exist.');
		}
	}

	private handleError(downloadId: string, msg: string, error: unknown) {
		toasts.error('Error', msg);
		console.error(msg, error);
		this.updateDownload(downloadId, {
			status: { state: 'ERROR', progress: null }
		});
	}
}

export const downloads = new DownloadsStore();
