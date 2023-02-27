import { get } from 'svelte/store';
import { session } from '$lib/stores/session';
import { env } from '$lib/config';

export class APIEndpointConstants {
	public static SEARCH = '/search';
	public static SESSION = '/session';
	public static DOWNLOADS = '/downloads';
}

export type RequestInfo = {
	endpoint: string;
	options: RequestInit;
};

/**
 * Return the url for a given api endpoint.
 * @param endpoint     The api endpoint you want.
 * @param urlParam     The url param for the endpoint you want.
 * @param queryParams  The query params for the endpoint you want.
 * @return             The url for that endpoint.
 */
export function getApiEndpoint(config: {
	base: APIEndpointConstants;
	method?: 'GET' | 'POST' | 'PUT' | 'DELETE' | 'PATCH' | 'OPTIONS';
	body?: BodyInit;
	urlParam?: string;
	queryParams?: Record<string, string | number>;
}): RequestInfo {
	let endpointString = `${env.serverAddress}${config.base}`;
	// If add urlParam to end of endpoint if needed
	if (config.urlParam !== undefined) {
		endpointString = `${endpointString}/${config.urlParam}`;
	}

	if (get(session)) {
		config.queryParams = {
			...config.queryParams,
			sessionId: get(session) ?? ''
		};
	}

	// Generate and add queryParam string for the key values specified
	if (config.queryParams !== undefined) {
		const queryParamsString = Object.keys(config.queryParams)
			.map((key) => `${key}=${config?.queryParams?.[key]}`)
			.join('&');
		endpointString = `${endpointString}?${queryParamsString}`;
	}

	const headers: Record<string, string> = {
		Accept: 'application/json',
		'Content-Type': 'application/json'
	};

	return {
		endpoint: endpointString,
		options: { credentials: 'include', method: config.method, body: config.body, headers }
	};
}
