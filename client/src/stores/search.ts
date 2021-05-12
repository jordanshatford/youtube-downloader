import { writable } from "svelte/store"
import type { VideoInfo } from "../utils/types"
import { getApiEndpoint } from "../utils/functions"
import { DEFAULT_RESULT_SIZE } from "../utils/constants"

function createSearchStore() {
    const API_ENDPOINT = "/search"
    const results: VideoInfo[] = []

    const { subscribe, set, update } = writable({
        term: "",
        numberResults: DEFAULT_RESULT_SIZE,
        results: results,
        loading: false,
    })

    function get(term: string, numberResults: number) {
        update(state => {
            state.term = term
            state.numberResults = numberResults
            state.loading = true
            return state
        })
        let url = getApiEndpoint(API_ENDPOINT, undefined, { "term": term, "results": numberResults })
        fetch(url).then(response => response.json()).then(results => {
            update(state => {
                state.results = results
                state.loading = false
                return state
            })
        })
    }

    return {
        subscribe,
        get,
        reset: () => set({ term: "", numberResults: DEFAULT_RESULT_SIZE, results: [], loading: false })
    }
}

export const search = createSearchStore()