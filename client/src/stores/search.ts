import { writable } from "svelte/store"
import type { SearchResult } from "../utils/types"
import { getApiEndpoint } from "../utils/functions"

function createSearchStore() {
    const API_ENDPOINT = "/search"
    const results: SearchResult[] = []
    const loading = false

    const { subscribe, set, update } = writable({
        "results": results,
        "loading": loading,
    })

    function search(term: string, numberResults: number) {
        update(state => {
            state.loading = true
            return state
        })
        let url = getApiEndpoint(API_ENDPOINT, undefined, { "term": term, "results": numberResults })
        fetch(url).then(results => results.json()).then(resultsJson => {
            update(state => {
                state.results = resultsJson
                state.loading = false
                return state
            })
        })
    }

    return {
        subscribe,
        search,
        reset: () => set({ results: [], loading: false })
    }
}

export const searchStore = createSearchStore()