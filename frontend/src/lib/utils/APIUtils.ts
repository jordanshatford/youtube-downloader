import { get } from 'svelte/store'
import { session } from '$lib/stores/session'

export class APIEndpointConstants {
	public static SEARCH = '/search'
	public static SESSION = '/session'
	public static DOWNLOADS = '/downloads'
}

export type RouteInfo = {
	endpoint: string
	options: RequestInit
}

export type QueryParamsOptions = {
	[key: string]: string | number
}

/**
 * Return the url for a given api endpoint.
 * @param endpoint     The api endpoint you want.
 * @param urlParam     The url param for the endpoint you want.
 * @param queryParams  The query params for the endpoint you want.
 * @return             The url for that endpoint.
 */
export function getApiEndpoint(
	config: {
		base: APIEndpointConstants
		method?: string
		body?: BodyInit
		urlParam?: string
		queryParams?: QueryParamsOptions
	}
): RouteInfo {
	let endpointString = `${import.meta.env.VITE_SERVER_ADDR}${config.base}`
	// If add urlParam to end of endpoint if needed
	if (config.urlParam !== undefined) {
		endpointString = `${endpointString}/${config.urlParam}`
	}

	if (get(session)) {
		config.queryParams = {
			...config.queryParams,
			'sessionId': get(session)
		}
	}

	// Generate and add queryParam string for the key values specified
	if (config.queryParams !== undefined) {
		const queryParamsString = Object.keys(config.queryParams)
			.map((key) => `${key}=${config.queryParams[key]}`)
			.join('&')
		endpointString = `${endpointString}?${queryParamsString}`
	}

	let headers: { [key: string]: string } = {
		Accept: 'application/json',
		'Content-Type': 'application/json'
	}

	return {
		endpoint: endpointString,
		options: { credentials: 'include', method: config.method, body: config.body, headers }
	}
}
