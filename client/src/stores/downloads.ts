import { get, writable } from "svelte/store"
import { session } from "./session"
import type { VideoInfo } from "../utils/types"
import { getApiEndpoint } from "../utils/functions"
import { saveAs } from "file-saver"
import { notifications } from "./notifications"
import { Status } from "../utils/types"

function createDownloadsStore() {
    const API_ENDPOINT = "/downloads"
    const downloads: { [key: string]: VideoInfo } = {}

    const { subscribe, set, update } = writable(downloads)

    let downloadStatus: EventSource = null

    function setupStatusListener() {
        downloadStatus = new EventSource(getApiEndpoint(API_ENDPOINT, "status", { "sessionId": get(session) }))

        downloadStatus.onmessage = function(event) {
            let data = JSON.parse(event.data)
            update(state => {
                let videoId = data["id"]
                let updatedStatus = data["status"]
                state[videoId].status = updatedStatus
                if (updatedStatus === Status.DONE) {
                    notifications.info("Download Complete", state[videoId].title)
                }
                return state
            })
        }
    }

    function add(downloadInfo: VideoInfo) {
        if (!(downloadInfo.id in downloads)) {
            // Add download to store using information we have already
            update(state => Object.assign(state, {[downloadInfo.id]: downloadInfo}))
            let url = getApiEndpoint(API_ENDPOINT, downloadInfo.id, { "sessionId": get(session) })
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

    function remove(id: string) {
        if (id in downloads) {
            update(state => {
                delete state[id]
                return state
            })
            let url = getApiEndpoint(API_ENDPOINT, id, { "sessionId": get(session) })
            fetch(url, { method: "DELETE" })
        }
    }

    function getFile(id: string) {
        if (id in downloads) {
            let url = getApiEndpoint(API_ENDPOINT, id, { "sessionId": get(session) })
            fetch(url).then(response => {
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