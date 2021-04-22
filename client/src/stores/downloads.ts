import { writable } from "svelte/store"
import type { DownloadInfo } from "../utils/types"

function createDownloadsStore() {
    const downloads = {}

    const { subscribe, set, update } = writable(downloads)

    function addDownload(downloadInfo: DownloadInfo) {
        if (!(downloadInfo.url in downloads))
            // Add download to store using information we have already
            update(currentDownloads => Object.assign(currentDownloads, {[downloadInfo.url]: downloadInfo}))
            console.error("Actual downloading not implemented yet!")
    }

    function removeDownload(url: string) {
        if (url in downloads)
            update(currentDownloads => {
                delete currentDownloads[url]
                return currentDownloads
            })
            console.error("Actual removing of download not implemented yet!")
    }

    return {
        subscribe,
        addDownload,
        removeDownload,
        reset: () => set({})
    }
}

export const downloadsStore = createDownloadsStore()