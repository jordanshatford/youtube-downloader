import { writable } from "svelte/store"
import { getApiEndpoint } from "../utils/functions"

function createSessionStore() {
    const API_ENDPOINT = "/session"
    const id: string = ""

    const { subscribe, set, update } = writable(id)

    async function setupSession() {
        let url = getApiEndpoint(API_ENDPOINT)
        let result = await fetch(url)
        let resultJson = await result.json()
        set(resultJson.sessionId)
    }

    return {
        subscribe,
        setupSession,
        reset: () => set(null)
    }
}

export const sessionStore = createSessionStore()
