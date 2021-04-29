import { writable } from "svelte/store"
import type { DownloadInfo } from "../utils/types"
import { getApiEndpoint } from "../utils/functions"
import { saveAs } from 'file-saver'

function createDownloadsStore() {
    const API_ENDPOINT = "/downloads"
    const downloads: { [key: string]: DownloadInfo } = {}

    const { subscribe, set, update } = writable(downloads)

    const downloadStatus = new EventSource("http://localhost:8000/api/downloads/status")

    downloadStatus.onmessage = function(event) {
        let data = JSON.parse(event.data)
        let id = data["id"]
        let status = data["status"]
        update(currentDownloads => {
            let x = currentDownloads[id]
            x.status = status
            currentDownloads[id] = x
            return currentDownloads
        })
    }

    function addDownload(downloadInfo: DownloadInfo) {
        if (!(downloadInfo.id in downloads)) {
            // Add download to store using information we have already
            update(currentDownloads => Object.assign(currentDownloads, {[downloadInfo.id]: downloadInfo}))
            let url = getApiEndpoint(API_ENDPOINT) + "/" + downloadInfo.id
            fetch(url, {
                method: 'POST',
                headers: {
                  'Accept': 'application/json',
                  'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    url: downloadInfo.url,
                })
            });
        }
    }

    function removeDownload(id: string) {
        if (id in downloads) {
            update(currentDownloads => {
                delete currentDownloads[id]
                return currentDownloads
            })
            let url = getApiEndpoint(API_ENDPOINT) + "/" + id
            fetch(url, {
                method: 'DELETE',
            })
        }
    }

    function downloadAudioFile(id: string) {
        if (id in downloads) {
            let x = downloads[id]
            let url = getApiEndpoint(API_ENDPOINT) + "/" + id
            fetch(url)
            .then(response => { 
                console.log(response)
                return response.blob()
            })
            .then(blob => saveAs(blob, `${x.title}.mp3`));
        }
    }

    return {
        subscribe,
        addDownload,
        removeDownload,
        downloadAudioFile,
        reset: () => set({})
    }
}

export const downloadsStore = createDownloadsStore()