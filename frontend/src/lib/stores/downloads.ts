import { writable } from 'svelte/store'
import type { VideoInfo } from '$lib/utils/types'
import { getApiEndpoint, APIEndpointConstants } from '$lib/utils/api'
import fileSaver from 'file-saver'
import { notifications } from '$lib/stores/notifications'
import { Status } from '$lib/utils/types'

function createDownloadsStore() {
	const downloads: { [key: string]: VideoInfo } = {}

	const { subscribe, set, update } = writable(downloads)

	let downloadStatus: EventSource = null

	function setupStatusListener() {
		const { endpoint } = getApiEndpoint({
			base: APIEndpointConstants.DOWNLOADS,
			urlParam: 'status'
		})
		downloadStatus = new EventSource(endpoint)

		downloadStatus.onmessage = function (event) {
			const data = JSON.parse(event.data)
			update((state) => {
				const videoId = data['id']
				const updatedStatus = data['status']
				state[videoId].status = updatedStatus
				switch (updatedStatus) {
					case Status.DONE:
						notifications.success('Download Complete', state[videoId].title)
						break
					case Status.ERROR:
					case Status.UNDEFINED:
						notifications.danger('Download Failed', state[videoId].title)
						break
					default:
						break
				}
				return state
			})
		}
	}

	function add(downloadInfo: VideoInfo) {
		if (downloadInfo.id in downloads) return

		// Add download to store using information we have already
		update((state) => Object.assign(state, { [downloadInfo.id]: downloadInfo }))
		const { endpoint, options } = getApiEndpoint({
			base: APIEndpointConstants.DOWNLOADS,
			method: 'POST',
			body: JSON.stringify({
				id: downloadInfo.id,
				url: downloadInfo.url
			})
		})
		fetch(endpoint, options)
	}

	function remove(id: string) {
		if (!(id in downloads)) return

		update((state) => {
			delete state[id]
			return state
		})
		const { endpoint, options } = getApiEndpoint({
			base: APIEndpointConstants.DOWNLOADS,
			method: 'DELETE',
			urlParam: id
		})
		fetch(endpoint, options)
	}

	function getFile(id: string) {
		if (!(id in downloads)) return

		const { endpoint, options } = getApiEndpoint({
			base: APIEndpointConstants.DOWNLOADS,
			method: 'GET',
			urlParam: id
		})
		fetch(endpoint, options).then(async (response) => {
			if (response.ok) {
				// The file blob is returned
				return response.blob().then((blob) => fileSaver.saveAs(blob, `${downloads[id].title}.mp3`))
			} else {
				// file was not found on the server a json error message is returned
				return response.json().then((data) => {
					notifications.danger(data['message'], data['detail'])
					remove(id)
				})
			}
		})
	}

	return {
		subscribe,
		setupStatusListener,
		add,
		remove,
		getFile,
		reset: () => set({})
	}
}

export const downloads = createDownloadsStore()
