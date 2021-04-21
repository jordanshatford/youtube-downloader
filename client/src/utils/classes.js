import { Status } from "./enums.js"

export class YoutubeDownloadInfo {
    constructor(id, url, title, thumbnail, status, downloadLink) {
        this.id = id
        this.url = url
        this.title = title
        this.thumbnail = thumbnail
        this.status = status
        this.downloadLink = downloadLink
    }

    static fromSearchResult(result) {
        return new YoutubeDownloadInfo(
            result.id,
            result.webpage_url,
            result.title,
            result.thumbnail,
            Status.UNDEFINED,
            null,          
        )
    }

    updateStatus(status, downloadLink = null) {
        this.status = status
        this.downloadLink = downloadLink
    }
}