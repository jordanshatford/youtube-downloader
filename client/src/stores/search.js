import { writable } from "svelte/store"

function createSearchStore() {
    const results = []
    const loading = false

    const { subscribe, set, update } = writable({
        "results": results,
        "loading": loading,
    })

    function setResults(res) {
        update(state => {
            state.results = res
            return state
        })
    }

    function setLoading(bool) {
        update(state => {
            state.loading = bool
            return state
        })
    }

    function search(term, numberResults) {
        setLoading(true)
        let url = `/api/search?term=${term}&results=${numberResults}`
        fetch(url).then(results => results.json()).then(resultsJson => {
            setResults(resultsJson)
            setLoading(false)
        })
    }

    return {
        subscribe,
        search,
        reset: () => set([])
    }
}

export const searchStore = createSearchStore()