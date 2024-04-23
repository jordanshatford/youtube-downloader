// This file is auto-generated by @hey-api/openapi-ts

import type { CancelablePromise } from './core/CancelablePromise';
import type { $OpenApiTs } from './types.gen';
import { OpenAPI } from './core/OpenAPI';
import { request as __request } from './core/request';

export class SearchService {
	/**
	 * Get Search
	 * @param data The data for the request.
	 * @param data.query
	 * @returns Video Successful Response
	 * @throws ApiError
	 */
	public static getSearch(
		data: $OpenApiTs['/search']['get']['req']
	): CancelablePromise<$OpenApiTs['/search']['get']['res'][200]> {
		return __request(OpenAPI, {
			method: 'GET',
			url: '/search',
			query: {
				query: data.query
			},
			errors: {
				403: 'Forbidden',
				404: 'Not Found',
				422: 'Validation Error'
			}
		});
	}

	/**
	 * Get Next Search
	 * @returns Video Successful Response
	 * @throws ApiError
	 */
	public static getNextSearch(): CancelablePromise<$OpenApiTs['/search/next']['get']['res'][200]> {
		return __request(OpenAPI, {
			method: 'GET',
			url: '/search/next',
			errors: {
				403: 'Forbidden',
				404: 'Not Found'
			}
		});
	}

	/**
	 * Get Video
	 * @param data The data for the request.
	 * @param data.id
	 * @returns Video Successful Response
	 * @throws ApiError
	 */
	public static getVideo(
		data: $OpenApiTs['/search/video']['get']['req']
	): CancelablePromise<$OpenApiTs['/search/video']['get']['res'][200]> {
		return __request(OpenAPI, {
			method: 'GET',
			url: '/search/video',
			query: {
				id: data.id
			},
			errors: {
				403: 'Forbidden',
				404: 'Not Found',
				422: 'Validation Error'
			}
		});
	}
}

export class SessionService {
	/**
	 * Get Session
	 * @returns Session Successful Response
	 * @throws ApiError
	 */
	public static getSession(): CancelablePromise<$OpenApiTs['/session']['get']['res'][200]> {
		return __request(OpenAPI, {
			method: 'GET',
			url: '/session'
		});
	}

	/**
	 * Delete Session
	 * @returns void Successful Response
	 * @throws ApiError
	 */
	public static deleteSession(): CancelablePromise<$OpenApiTs['/session']['delete']['res'][204]> {
		return __request(OpenAPI, {
			method: 'DELETE',
			url: '/session',
			errors: {
				403: 'Forbidden'
			}
		});
	}

	/**
	 * Get Session Validate
	 * @returns Session Successful Response
	 * @throws ApiError
	 */
	public static getSessionValidate(): CancelablePromise<
		$OpenApiTs['/session/validate']['get']['res'][200]
	> {
		return __request(OpenAPI, {
			method: 'GET',
			url: '/session/validate',
			errors: {
				403: 'Forbidden'
			}
		});
	}
}

export class DownloadsService {
	/**
	 * Get Downloads
	 * @returns Download Successful Response
	 * @throws ApiError
	 */
	public static getDownloads(): CancelablePromise<$OpenApiTs['/downloads']['get']['res'][200]> {
		return __request(OpenAPI, {
			method: 'GET',
			url: '/downloads',
			errors: {
				403: 'Forbidden'
			}
		});
	}

	/**
	 * Put Downloads
	 * @param data The data for the request.
	 * @param data.requestBody
	 * @returns Download Successful Response
	 * @throws ApiError
	 */
	public static putDownloads(
		data: $OpenApiTs['/downloads']['put']['req']
	): CancelablePromise<$OpenApiTs['/downloads']['put']['res'][200]> {
		return __request(OpenAPI, {
			method: 'PUT',
			url: '/downloads',
			body: data.requestBody,
			mediaType: 'application/json',
			errors: {
				403: 'Forbidden',
				422: 'Validation Error'
			}
		});
	}

	/**
	 * Post Downloads
	 * @param data The data for the request.
	 * @param data.requestBody
	 * @returns Download Successful Response
	 * @throws ApiError
	 */
	public static postDownloads(
		data: $OpenApiTs['/downloads']['post']['req']
	): CancelablePromise<$OpenApiTs['/downloads']['post']['res'][201]> {
		return __request(OpenAPI, {
			method: 'POST',
			url: '/downloads',
			body: data.requestBody,
			mediaType: 'application/json',
			errors: {
				403: 'Forbidden',
				422: 'Validation Error'
			}
		});
	}

	/**
	 * Get Downloads Options
	 * @returns AvailableDownloadOptions Successful Response
	 * @throws ApiError
	 */
	public static getDownloadsOptions(): CancelablePromise<
		$OpenApiTs['/downloads/options']['get']['res'][200]
	> {
		return __request(OpenAPI, {
			method: 'GET',
			url: '/downloads/options',
			errors: {
				403: 'Forbidden'
			}
		});
	}

	/**
	 * Get Download
	 * @param data The data for the request.
	 * @param data.downloadId
	 * @returns Download Successful Response
	 * @throws ApiError
	 */
	public static getDownload(
		data: $OpenApiTs['/downloads/{download_id}']['get']['req']
	): CancelablePromise<$OpenApiTs['/downloads/{download_id}']['get']['res'][200]> {
		return __request(OpenAPI, {
			method: 'GET',
			url: '/downloads/{download_id}',
			path: {
				download_id: data.downloadId
			},
			errors: {
				403: 'Forbidden',
				404: 'Not Found',
				422: 'Validation Error'
			}
		});
	}

	/**
	 * Delete Download
	 * @param data The data for the request.
	 * @param data.downloadId
	 * @returns void Successful Response
	 * @throws ApiError
	 */
	public static deleteDownload(
		data: $OpenApiTs['/downloads/{download_id}']['delete']['req']
	): CancelablePromise<$OpenApiTs['/downloads/{download_id}']['delete']['res'][204]> {
		return __request(OpenAPI, {
			method: 'DELETE',
			url: '/downloads/{download_id}',
			path: {
				download_id: data.downloadId
			},
			errors: {
				403: 'Forbidden',
				404: 'Not Found',
				422: 'Validation Error'
			}
		});
	}

	/**
	 * Get Download File
	 * @param data The data for the request.
	 * @param data.downloadId
	 * @returns binary Successful Response
	 * @throws ApiError
	 */
	public static getDownloadFile(
		data: $OpenApiTs['/downloads/{download_id}/file']['get']['req']
	): CancelablePromise<$OpenApiTs['/downloads/{download_id}/file']['get']['res'][200]> {
		return __request(OpenAPI, {
			method: 'GET',
			url: '/downloads/{download_id}/file',
			path: {
				download_id: data.downloadId
			},
			errors: {
				403: 'Forbidden',
				404: 'Not Found',
				422: 'Validation Error'
			}
		});
	}
}
