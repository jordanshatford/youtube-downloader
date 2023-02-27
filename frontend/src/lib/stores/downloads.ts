import { writable, get } from 'svelte/store';
import fileSaver from 'file-saver';
import type { VideoInfo } from '$lib/utils/types';
import { getApiEndpoint, APIEndpointConstants } from '$lib/utils/api';
import { Status, AudioFormat } from '$lib/utils/types';
import { settings } from '$lib/stores/settings';

function createDownloadsStore() {
	const downloads: Record<string, VideoInfo> = {};

	const { subscribe, set, update } = writable(downloads);

	let downloadStatus: EventSource | null = null;

	function setupStatusListener() {
		const { endpoint } = getApiEndpoint({
			base: APIEndpointConstants.DOWNLOADS,
			urlParam: 'status'
		});
		downloadStatus = new EventSource(endpoint);

		downloadStatus.onmessage = function (event) {
			const data = JSON.parse(event.data);
			update((state) => {
				const videoId = data['id'];
				const updatedStatus = data['status'];
				state[videoId].status = updatedStatus;
				return state;
			});
		};
	}

	function add(downloadInfo: VideoInfo) {
		if (downloadInfo.id in downloads) return;

		downloadInfo = {
			...downloadInfo,
			options: {
				format: get(settings).format ?? AudioFormat.MP3
			}
		};

		// Add download to store using information we have already
		update((state) => Object.assign(state, { [downloadInfo.id]: downloadInfo }));
		const { endpoint, options } = getApiEndpoint({
			base: APIEndpointConstants.DOWNLOADS,
			method: 'POST',
			body: JSON.stringify({
				id: downloadInfo.id,
				url: downloadInfo.url,
				options: downloadInfo.options
			})
		});
		fetch(endpoint, options).catch((err) => {
			console.error('Failed to add video to download ', err);
			update((state) => {
				state[downloadInfo.id].status = Status.ERROR;
				return state;
			});
		});
	}

	function remove(id: string) {
		if (!(id in downloads)) return;

		update((state) => {
			delete state[id];
			return state;
		});
		const { endpoint, options } = getApiEndpoint({
			base: APIEndpointConstants.DOWNLOADS,
			method: 'DELETE',
			urlParam: id
		});
		fetch(endpoint, options);
	}

	function getFile(id: string) {
		if (!(id in downloads)) return;

		update((state) => {
			state[id].awaitingFileBlob = true;
			return state;
		});
		const { endpoint, options } = getApiEndpoint({
			base: APIEndpointConstants.DOWNLOADS,
			method: 'GET',
			urlParam: id
		});
		fetch(endpoint, options).then(async (response) => {
			if (response.ok) {
				// The file blob is returned
				return response.blob().then((blob) => {
					update((state) => {
						state[id].awaitingFileBlob = false;
						return state;
					});
					fileSaver.saveAs(blob, `${downloads[id].title}.${downloads?.[id]?.options?.format}`);
				});
			} else {
				// file was not found on the server a json error message is returned
				return response.json().then(() => {
					remove(id);
				});
			}
		});
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
