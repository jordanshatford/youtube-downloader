import { writable } from "svelte/store"
import { getApiEndpoint } from "../utils/functions"

const id: string = ""
export const sessionStore = writable(id)

const API_ENDPOINT = "/session"
export const sessionEndpoint = getApiEndpoint(API_ENDPOINT)
