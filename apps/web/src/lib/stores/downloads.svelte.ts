import { SESSION_ID_KEY } from '$lib/api';
import { settings } from '$lib/stores/settings.svelte';
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
import { toast } from '@yd/ui';

class DownloadsStore {
	public downloads = $state<Record<string, Download>>({});

	private async setupStatusMonitoring() {
		const { stream } = await getDownloadsStatus({
			query: { session_id: localStorage.getItem(SESSION_ID_KEY) ?? '' }
		});
		for await (const event of stream) {
			// https://github.com/hey-api/openapi-ts/issues/2921
			const download = event as Download;
			this.updateDownload(download.video.id, download);
		}
	}

	public async init() {
		// Setup listener for status updates of any downloads.
		this.setupStatusMonitoring();
		// Get all previous downloads still available.
		const { data: downloads } = await getDownloads();
		if (downloads) {
			this.downloads = downloads.reduce(
				(acc, curr) => {
					acc[curr.video.id] = curr;
					return acc;
				},
				{} as Record<string, Download>
			);
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
			toast.success('Download removed successfully.');
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
		} else {
			console.error('Attempted to update download that does not exist.');
		}
	}

	private handleError(downloadId: string, msg: string, error: unknown) {
		toast.error(msg);
		console.error(msg, error);
		this.updateDownload(downloadId, {
			status: { state: 'ERROR', progress: null }
		});
	}
}

export const downloads = new DownloadsStore();
