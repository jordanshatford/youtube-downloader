import { writable } from "svelte/store"

function createSearchStore() {
    const STORE_API_PREFIX = "/api/search"
    const results = []
    const loading = false

    const { subscribe, set, update } = writable({
        "results": results,
        "loading": loading,
    })

    function search(term, numberResults) {
        update(state => {
            state.loading = true
            return state
        })
        let url = `${STORE_API_PREFIX}?term=${term}&results=${numberResults}`
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
        reset: () => set([])
    }
}

export const searchStore = createSearchStore()