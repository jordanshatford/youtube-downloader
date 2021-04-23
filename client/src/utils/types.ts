// The status of a video being converted to MP3
export enum Status {
    WAITING = "WAITING",
    DOWNLOADING = "DOWNLOADING",
    PROCESSING = "PROCESSING",
    DONE = "DONE",
    UNDEFINED = "UNDEFINED",
}

// The download info of a video
export type DownloadInfo = {
    id: string
    url: string
    title: string
    thumbnail: string
    status: Status
}

// The search results from searching for a video
export type SearchResult = {
    id: string
    webpage_url: string
    thumbnail: string
    title: string
    duration: number
    description: string
    channel_url: string
    channel: string
}

// A route for svelte-router-spa
export type Route = {
    label: string
    path: string
}