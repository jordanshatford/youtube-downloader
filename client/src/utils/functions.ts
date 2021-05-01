import { SERVER_IP, SERVER_PORT } from "./constants"

/**
 * Return the url for a given api endpoint.
 * @param endpoint     The api endpoint you want.
 * @param urlParam     The url param for the endpoint you want.
 * @param queryParams  The query params for the endpoint you want.
 * @return             The url for that endpoint.
 */
export function getApiEndpoint(endpoint: string, urlParam?: string, queryParams?: {[key: string]: string | number}): string {
    let endpointString = `http://${SERVER_IP}:${SERVER_PORT}/api${endpoint}`

    // If add urlParam to end of endpoint if needed
    if (urlParam !== undefined) {
        endpointString = `${endpointString}/${urlParam}`
    }

    // Generate and add queryParam string for the key values specified
    if (queryParams !== undefined) {
        let queryParamsString = Object.keys(queryParams).map(key => `${key}=${queryParams[key]}`).join("&")
        endpointString = `${endpointString}?${queryParamsString}`
    }
    return endpointString
}

/**
 * Truncate a string to a specified size.
 * @param str  The string to be truncated.
 * @param n    The length to make the truncated string.
 * @return     The string properly truncated.
 */
export function truncate(str: string, n: number): string {
    return (str.length > n) ? str.substring(0, n-1) + "..." : str
}

/**
 * Format seconds into proper hours, minutes, and seconds string.
 * @param duration  The number of seconds.
 * @return          The string representing the seconds in HH:MM:SS format.
 */
export function formatSeconds(duration: number): string {
    let hrs = ~~(duration/3600)
    let mins = ~~((duration % 3600) / 60)
    let secs = ~~duration % 60

    let result = ""
    if (hrs > 0) {
        result += "" + hrs + ":" + (mins < 10 ? "0" : "")
    }

    result += "" + mins + ":" + (secs < 10 ? "0" : "")
    result += "" + secs
    return result
}
