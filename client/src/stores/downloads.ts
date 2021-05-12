import { get, writable } from "svelte/store"
import { session } from "./session"
import type { VideoInfo } from "../utils/types"
import { getApiEndpoint, truncate } from "../utils/functions"
import { MAX_TITLE_LENGTH } from "../utils/constants"
import { saveAs } from "file-saver"
import { notifications } from "./notifications"
import { Status } from "../utils/types"

function createDownloadsStore() {
    const API_ENDPOINT = "/downloads"
    const downloads: { [key: string]: VideoInfo } = {}

    const { subscribe, set, update } = writable(downloads)

    let downloadStatus: EventSource = null

    function setupStatusListener() {
        downloadStatus = new EventSource(getApiEndpoint(API_ENDPOINT, "status", getSessionData()))

        downloadStatus.onmessage = function(event) {
            let data = JSON.parse(event.data)
            update(state => {
                let videoId = data["id"]
                let updatedStatus = data["status"]
                state[videoId].status = updatedStatus
                if (updatedStatus === Status.DONE) {
                    notifications.info("Download Complete", truncate(state[videoId].title, MAX_TITLE_LENGTH))
                }
                return state
            })
        }
    }

    function add(downloadInfo: VideoInfo) {
        if (downloadInfo.id in downloads)
            return
    
        // Add download to store using information we have already
        update(state => Object.assign(state, {[downloadInfo.id]: downloadInfo}))
        let url = getApiEndpoint(API_ENDPOINT, downloadInfo.id, getSessionData())
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

    function remove(id: string) {
        if (!(id in downloads))
            return

        update(state => {
            delete state[id]
            return state
        })
        let url = getApiEndpoint(API_ENDPOINT, id, getSessionData())
        fetch(url, { method: "DELETE" })
    }

    function getFile(id: string) {
        if (!(id in downloads))
            return

        let url = getApiEndpoint(API_ENDPOINT, id, getSessionData())
        fetch(url).then(async response => {
            if (response.ok) {
                // The file blob is returned
                return response.blob().then(blob => saveAs(blob, `${downloads[id].title}.mp3`))
            } else {
                // file was not found on the server a json error message is returned
                return response.json().then(data => {
                    notifications.danger(data["message"], data["detail"], 5000)
                    remove(id)
                })
            }
        })
    }

    function getSessionData() {
        return { "sessionId": get(session) }
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