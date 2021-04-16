import { writable } from "svelte/store"

function createDownloadsStore() {
    const downloads = {}

    const { subscribe, set, update } = writable(downloads)

    function addDownload(downloadInfo) {
        if (!(downloadInfo.url in downloads))
            // Add download to store using information we have already
            update(currentDownloads => Object.assign(currentDownloads, {[downloadInfo.url]: downloadInfo}))
            console.error("Actual downloading not implemented yet!")
    }

    function removeDownload(url) {
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