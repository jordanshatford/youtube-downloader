import { get, writable } from "svelte/store"
import { sessionStore } from "./session"
import type { VideoInfo } from "../utils/types"
import { getApiEndpoint } from "../utils/functions"
import { saveAs } from 'file-saver'

function createDownloadsStore() {
    const API_ENDPOINT = "/downloads"
    const downloads: { [key: string]: VideoInfo } = {}

    const { subscribe, set, update } = writable(downloads)

    let downloadStatus: EventSource = null

    function setupDownloadStatusListener() {
        downloadStatus = new EventSource(getApiEndpoint(API_ENDPOINT, "status", { "sessionId": get(sessionStore) }))

        downloadStatus.onmessage = function(event) {
            let data = JSON.parse(event.data)
            update(currentDownloads => {
                currentDownloads[data["id"]].status = data["status"]
                return currentDownloads
            })
        }
    }

    function addDownload(downloadInfo: VideoInfo) {
        if (!(downloadInfo.id in downloads)) {
            // Add download to store using information we have already
            update(currentDownloads => Object.assign(currentDownloads, {[downloadInfo.id]: downloadInfo}))
            let url = getApiEndpoint(API_ENDPOINT, downloadInfo.id, { "sessionId": get(sessionStore) })
            fetch(url, {
                method: "POST",
                headers: {
                  "Accept": "application/json",
                  "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    url: downloadInfo.url,
                })
            })
        }
    }

    function removeDownload(id: string) {
        if (id in downloads) {
            update(currentDownloads => {
                delete currentDownloads[id]
                return currentDownloads
            })
            let url = getApiEndpoint(API_ENDPOINT, id, { "sessionId": get(sessionStore) })
            fetch(url, { method: "DELETE" })
        }
    }

    function downloadAudioFile(id: string) {
        if (id in downloads) {
            let url = getApiEndpoint(API_ENDPOINT, id, { "sessionId": get(sessionStore) })
            fetch(url).then(response => {
                return response.blob()
            })
            .then(blob => saveAs(blob, `${downloads[id].title}.mp3`))
        }
    }

    return {
        subscribe,
        setupDownloadStatusListener,
        addDownload,
        removeDownload,
        downloadAudioFile,
        reset: () => set({})
    }
}

export const downloadsStore = createDownloadsStore()