import Search from "./routes/Search.svelte"
import Downloads from "./routes/Downloads.svelte"
import DefaultLayout from "./routes/layout/Default.svelte"

const routes = [
    {
        name: "/",
        redirectTo: "search",
    },
    {
        name: "/search",
        component: Search,
        layout: DefaultLayout,
    },
    {
        name: "/downloads",
        component: Downloads,
        layout: DefaultLayout,
    }
]
  
export { routes }