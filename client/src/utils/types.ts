// The status of a video being converted to MP3
export enum Status {
    WAITING = "WAITING",
    DOWNLOADING = "DOWNLOADING",
    PROCESSING = "PROCESSING",
    DONE = "DONE",
    UNDEFINED = "UNDEFINED",
}

export enum Theme {
    LIGHT = "light",
    DARK = "dark",
}

// The information about a specific youtube video
export type VideoInfo = {
    id: string
    url: string
    title: string
    thumbnail: string
    duration?: string
    channel?: string
    channelUrl?: string
    channelThumbnail?: string
    status?: Status
}
