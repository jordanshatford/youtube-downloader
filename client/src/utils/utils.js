/**
 * Truncate a string to a specified size.
 * @param  {String} str  The string to be truncated.
 * @param  {Number} n    The length to make the truncated string.
 * @return {String}      The string properly truncated.
 */
export function truncate(str, n) {
    return (str.length > n) ? str.substring(0, n-1) + "..." : str
}

/**
 * Format seconds into proper hours, minutes, and seconds string.
 * @param  {Number} duration  The number of seconds.
 * @return {String}           The string representing the seconds in HH:MM:SS format.
 */
export function formatSeconds(duration) {
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