import { Status } from "./types"
import type { DownloadInfo, SearchResult } from "./types"

export class YoutubeDownloadInfo {
    id: string
    url: string
    title: string
    thumbnail: string
    status: Status
    downloadLink: string | null

    constructor(downloadInfo: DownloadInfo) {
        this.id = downloadInfo.id
        this.url = downloadInfo.url
        this.title = downloadInfo.title
        this.thumbnail = downloadInfo.thumbnail
        this.status = downloadInfo.status
        this.downloadLink = downloadInfo.downloadLink
    }

    static fromSearchResult(result: SearchResult) {
        return new YoutubeDownloadInfo({
            id: result.id,
            url: result.webpage_url,
            title: result.title,
            thumbnail: result.thumbnail,
            status: Status.UNDEFINED,
            downloadLink: null
        })
    }

    updateStatus(status: Status, downloadLink: string | null = null) {
        this.status = status
        this.downloadLink = downloadLink
    }
}