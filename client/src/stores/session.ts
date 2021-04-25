import ReconnectingWebsocket from "reconnecting-websocket"
import { writable } from "svelte/store"
import { getApiEndpoint } from "../utils/functions"

function createSessionStore() {
    const API_ENDPOINT = "/api/session"
    const id: string = ""
    let socket: ReconnectingWebsocket = null

    const { subscribe, set, update } = writable(id)

    async function setupSession() {
        let url = getApiEndpoint(API_ENDPOINT)
        let result = await fetch(url)
        let resultJson = await result.json()
        let sess = resultJson.sessionId
        console.log("Session ID: ", sess)
        set(sess)
        socket = new ReconnectingWebsocket("ws://localhost:8000/ws/session")
		socket.onopen = function() {
			socket.send(sess);
			console.log("Socket Open: ", sess)
		};
		socket.onclose = function(evt) {
			console.log("Socket Closed: ", sess);
		};
		socket.onmessage = function(evt) {
			console.log("Message: ", sess)
		};
    }

    return {
        subscribe,
        setupSession,
        reset: () => set(null)
    }
}

export const sessionStore = createSessionStore()
