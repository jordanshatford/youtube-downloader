import { writable } from "svelte/store"

function createSearchStore() {
    const results = []
    const loading = false

    const { subscribe, set, update } = writable({
        "results": results,
        "loading": loading,
    })

    function updateContext(results=null, loading=null) {
        update(state => {
            if (results != null)
                state.results = results
            if (loading != null)
                state.loading = loading
            return state
        })
    }

    function search(term, numberResults) {
        updateContext(null, true)
        let url = `/api/search?term=${term}&results=${numberResults}`
        fetch(url).then(results => results.json()).then(resultsJson => {
            updateContext(resultsJson, false)
        })
    }

    return {
        subscribe,
        search,
        reset: () => set([])
    }
}

export const searchStore = createSearchStore()