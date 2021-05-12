import { writable } from "svelte/store"
import { getApiEndpoint } from "../utils/functions"
import { notifications } from "./notifications"

function createSessionStore() {
    const API_ENDPOINT = "/session"
    const RE_ATTEMPT_INTERVAL = 10000

    const { subscribe, set } = writable(null)

    async function setup() {
        let url = getApiEndpoint(API_ENDPOINT)
        await fetch(url).then(response => {
            return response.json()
        }).then(data => {
            set(data?.sessionId)
        }).catch(_err => {
            notifications.warning("Connection Failed", "Could not connect to internal server. Retrying in 10 seconds.", 5000)
            _reAttempt()
        })
    }

    async function _reAttempt() {
        setTimeout(() => {
            setup()
        }, RE_ATTEMPT_INTERVAL)
    }

    return {
        subscribe,
        setup,
        reset: () => set(null)
    }
}

export const session = createSessionStore()
