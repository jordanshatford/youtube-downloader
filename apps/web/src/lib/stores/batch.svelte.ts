import { getSessionID } from '$lib/api';
import { settings } from '$lib/stores/settings.svelte';
import { saveAs } from '$lib/utils/files';

import type { BatchDownload, Download } from '@yd/client';
import {
	deleteBatch,
	getBatch,
	getBatchFile,
	getBatchStatus,
	postBatch,
	putBatch
} from '@yd/client';
import { toast } from '@yd/ui';

/**
 * Check if some text is a YouTube URL.
 * @param text - the text to check.
 * @returns true if the URL is for YouTube, false otherwise.
 */
function isYouTubeUrl(text: string): boolean {
	try {
		const url = new URL(text);
		const isYouTube = ['youtube.com', 'youtu.be'].some((u) => url.hostname.includes(u));
		const hasVideo = url.searchParams.has('v');
		const hasPlaylist = url.searchParams.has('list');
		return isYouTube && (hasVideo || hasPlaylist);
	} catch {
		return false;
	}
}

class BatchStore {
	public text = $state<string>('');
	public batch = $state<BatchDownload | undefined>();

	// Derived by the input text these URLs are all unique and valid YouTube URLs.
	// This does not guarentee that the URLs are all videos available to the user.
	public textUniqueUrls = $derived.by<string[]>(() => {
		const trimmed = this.text
			.split(/[\s]+/) // \s = space, tab, newline, etc.
			.map((s) => s.trim());

		const unique = [...new Set(trimmed)];
		const filtered = unique.filter((u) => u && isYouTubeUrl(u));
		return filtered;
	});

	public hasURLs = $derived<boolean>(this.textUniqueUrls.length > 0);
	public hasTooManyURLs = $derived<boolean>(this.textUniqueUrls.length > 25);

	// Get the current actively downloading item in the batch. This puts it in a format
	// more easily displayable to the user, since details about it are stored accross
	// different parts of the batch downloads entries.
	public current = $derived.by<Omit<Download, 'options'> | undefined>(() => {
		const items = Object.entries(this.batch?.status.items ?? []);
		if (items.length === 0) {
			return undefined;
		}
		const [lastID, lastStatus] = items[items.length - 1];
		const videos = this.batch?.videos ?? {};
		return { video: videos[lastID], status: lastStatus };
	});

	// Get all non currently downloading videos. This also puts it in a format more
	// easily displayable to the user. These are separated to allow hiding this list
	// since it could be very long. Instead the user can manually expand it.
	public others = $derived.by<Omit<Download, 'options'>[]>(() => {
		const items = Object.entries(this.batch?.status?.items ?? []);
		const filtered = items.filter(([id]) => id !== this.current?.video.id);
		const videos = this.batch?.videos ?? {};
		return filtered
			.map(([id, status]) => {
				return { video: videos[id], status };
			})
			.reverse();
	});

	// If the batch is done and file should be downloadable.
	public isDownloadDisabled = $derived<boolean>(!(this.batch?.status.overall.state === 'DONE'));
	// If the batch download has errored.
	public isOverallError = $derived<boolean>(this.batch?.status.overall.state === 'ERROR');
	// If the batch has errored out, and can be retried.
	public isRetryDisabled = $derived<boolean>(!this.isOverallError);
	// If the batch is in a deletable state, i.e. if it is completed or has failed.
	public isDeleteDisabled = $derived<boolean>(
		!this.batch || !['DONE', 'ERROR'].includes(this.batch?.status.overall.state)
	);

	// If the batch is loading (i.e. currently downloading or processing.)
	public isLoading = $derived.by<boolean>(() => {
		if (this.batch === undefined) {
			return false;
		}
		return !['DONE', 'ERROR'].includes(this.batch.status.overall.state);
	});

	// The number of done downloads in the batch. I.e. for overall progress tracking.
	public nDone = $derived<number>(this.batch?.status.overall.downloaded_bytes ?? 0);
	// The number of total downloads in the batch. I.e. for overall progress tracking. Note: this could change as the download
	// is ongoing. For example, if a playlist is specified, the total number of downloads will update as we know about more
	// videos that are available for download.
	public nTotal = $derived<number>(
		this.batch?.status.overall.total_bytes ?? this.textUniqueUrls.length
	);

	private async setupStatusMonitoring(): Promise<void> {
		const { stream } = await getBatchStatus({
			query: { session_id: getSessionID() }
		});
		for await (const event of stream) {
			// TODO(jordan): https://github.com/hey-api/openapi-ts/issues/2921
			const batch = event as BatchDownload;
			this.updateBatch(batch);
		}
	}

	public async init(): Promise<void> {
		// Setup listener for status updates of any downloads.
		this.setupStatusMonitoring();
		// Get all previous downloads still available.
		try {
			const { data: batch } = await getBatch();
			if (batch) {
				this.batch = batch;
				this.text = batch.urls.join('\n');
			} else {
				this.batch = undefined;
			}
		} catch {
			this.batch = undefined;
		}
	}

	public async add(): Promise<void> {
		if (this.batch !== undefined) return;

		// Add initial value for the batch download.
		this.batch = {
			urls: this.textUniqueUrls,
			status: {
				overall: { state: 'WAITING', progress: null },
				items: {}
			},
			videos: {},
			options: settings.settings
		};

		try {
			const { data: result } = await postBatch({
				body: this.batch
			});
			if (result) {
				this.updateBatch(result);
			}
		} catch (err) {
			this.handleError(`Failed to add batch of downloads.`, err);
		}
	}

	public async restart(): Promise<void> {
		if (this.batch === undefined) return;

		const batch = this.batch;

		try {
			const { data: result } = await putBatch({
				body: batch
			});
			if (result) {
				this.batch = result;
			}
		} catch (err) {
			this.handleError(`Failed to restart batch of downloads.`, err);
		}
	}

	public async remove(): Promise<void> {
		if (this.batch === undefined) return;

		try {
			await deleteBatch();
			toast.success('Batch download removed successfully.');
			this.text = '';
			this.batch = undefined;
		} catch (err) {
			this.handleError('Failed to remove batch of downloads.', err);
		}
	}

	public async getFile(): Promise<void> {
		if (this.batch === undefined) return;

		try {
			const { data: file } = await getBatchFile();
			if (file) {
				const filename = 'batch.zip';
				saveAs(file, filename);
			}
		} catch (err) {
			this.handleError('Failed to get file for batch of downloads.', err);
		}
	}

	private updateBatch(updatedValue: Partial<BatchDownload>): void {
		if (this.batch !== undefined) {
			const value: BatchDownload | undefined = {
				...this.batch,
				status: {
					overall: {
						...this.batch.status.overall,
						...(updatedValue.status?.overall ?? {})
					},
					items: {
						...this.batch.status.items,
						...(updatedValue.status?.items ?? {})
					}
				},
				videos: {
					...this.batch.videos,
					...(updatedValue.videos ?? {})
				}
			};
			this.batch = value;
		} else {
			console.error('Attempted to update batch of downloads that does not exist.');
		}
	}

	private handleError(msg: string, error: unknown): void {
		toast.error(msg);
		console.error(msg, error);
		this.updateBatch({
			status: {
				overall: { state: 'ERROR', progress: null },
				items: {}
			}
		});
	}
}

export const batch = new BatchStore();
