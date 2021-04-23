import { writable } from "svelte/store"
import type { DownloadInfo } from "../utils/types"

function createDownloadsStore() {
    const downloads = {}

    const { subscribe, set, update } = writable(downloads)

    function addDownload(downloadInfo: DownloadInfo) {
        if (!(downloadInfo.id in downloads))
            // Add download to store using information we have already
            update(currentDownloads => Object.assign(currentDownloads, {[downloadInfo.id]: downloadInfo}))
            console.error("Actual downloading not implemented yet!")
    }

    function removeDownload(id: string) {
        if (id in downloads)
            update(currentDownloads => {
                delete currentDownloads[id]
                return currentDownloads
            })
            console.error("Actual removing of download not implemented yet!")
    }

    function downloadAudioFile(id: string) {
        console.error("Actual downloading of audio file not implemented yet!")
    }

    function downloadAllAudioFiles() {
        console.error("Downloading videos is not implemented yet!")
    }

    return {
        subscribe,
        addDownload,
        removeDownload,
        downloadAudioFile,
        downloadAllAudioFiles,
        reset: () => set({})
    }
}

export const downloadsStore = createDownloadsStore()