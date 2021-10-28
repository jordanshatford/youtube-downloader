/**
 * Return the url for a given api endpoint.
 * @param endpoint     The api endpoint you want.
 * @param urlParam     The url param for the endpoint you want.
 * @param queryParams  The query params for the endpoint you want.
 * @return             The url for that endpoint.
 */
export function getApiEndpoint(
	endpoint: string,
	urlParam?: string,
	queryParams?: { [key: string]: string | number }
): string {
	let endpointString = `${import.meta.env.VITE_SERVER_ADDR}/api${endpoint}`
	// If add urlParam to end of endpoint if needed
	if (urlParam !== undefined) {
		endpointString = `${endpointString}/${urlParam}`
	}

	// Generate and add queryParam string for the key values specified
	if (queryParams !== undefined) {
		const queryParamsString = Object.keys(queryParams)
			.map((key) => `${key}=${queryParams[key]}`)
			.join('&')
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
	return str.length > n ? str.substring(0, n - 1) + '...' : str
}