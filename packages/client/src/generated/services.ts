import type { CancelablePromise } from './core/CancelablePromise';
import { OpenAPI } from './core/OpenAPI';
import { request as __request } from './core/request';
import type { SearchData, SessionData, DownloadsData } from './models';

export class SearchService {
	/**
	 * Get Search
	 * @returns Video Successful Response
	 * @throws ApiError
	 */
	public static getSearch(
		data: SearchData['payloads']['GetSearch']
	): CancelablePromise<SearchData['responses']['GetSearch']> {
		const { query } = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/search',
			query: {
				query
			},
			errors: {
				403: `Forbidden`,
				404: `Not Found`,
				422: `Validation Error`
			}
		});
	}

	/**
	 * Get Next Search
	 * @returns Video Successful Response
	 * @throws ApiError
	 */
	public static getNextSearch(): CancelablePromise<SearchData['responses']['GetNextSearch']> {
		return __request(OpenAPI, {
			method: 'GET',
			url: '/search/next',
			errors: {
				403: `Forbidden`,
				404: `Not Found`
			}
		});
	}

	/**
	 * Get Video
	 * @returns Video Successful Response
	 * @throws ApiError
	 */
	public static getVideo(
		data: SearchData['payloads']['GetVideo']
	): CancelablePromise<SearchData['responses']['GetVideo']> {
		const { id } = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/search/video',
			query: {
				id
			},
			errors: {
				403: `Forbidden`,
				404: `Not Found`,
				422: `Validation Error`
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
	public static getSession(): CancelablePromise<SessionData['responses']['GetSession']> {
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
	public static deleteSession(): CancelablePromise<SessionData['responses']['DeleteSession']> {
		return __request(OpenAPI, {
			method: 'DELETE',
			url: '/session',
			errors: {
				403: `Forbidden`
			}
		});
	}

	/**
	 * Get Session Validate
	 * @returns Session Successful Response
	 * @throws ApiError
	 */
	public static getSessionValidate(): CancelablePromise<
		SessionData['responses']['GetSessionValidate']
	> {
		return __request(OpenAPI, {
			method: 'GET',
			url: '/session/validate',
			errors: {
				403: `Forbidden`
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
	public static getDownloads(): CancelablePromise<DownloadsData['responses']['GetDownloads']> {
		return __request(OpenAPI, {
			method: 'GET',
			url: '/downloads',
			errors: {
				403: `Forbidden`
			}
		});
	}

	/**
	 * Put Downloads
	 * @returns Download Successful Response
	 * @throws ApiError
	 */
	public static putDownloads(
		data: DownloadsData['payloads']['PutDownloads']
	): CancelablePromise<DownloadsData['responses']['PutDownloads']> {
		const { requestBody } = data;
		return __request(OpenAPI, {
			method: 'PUT',
			url: '/downloads',
			body: requestBody,
			mediaType: 'application/json',
			errors: {
				403: `Forbidden`,
				422: `Validation Error`
			}
		});
	}

	/**
	 * Post Downloads
	 * @returns Download Successful Response
	 * @throws ApiError
	 */
	public static postDownloads(
		data: DownloadsData['payloads']['PostDownloads']
	): CancelablePromise<DownloadsData['responses']['PostDownloads']> {
		const { requestBody } = data;
		return __request(OpenAPI, {
			method: 'POST',
			url: '/downloads',
			body: requestBody,
			mediaType: 'application/json',
			errors: {
				403: `Forbidden`,
				422: `Validation Error`
			}
		});
	}

	/**
	 * Get Downloads Options
	 * @returns AvailableDownloadOptions Successful Response
	 * @throws ApiError
	 */
	public static getDownloadsOptions(): CancelablePromise<
		DownloadsData['responses']['GetDownloadsOptions']
	> {
		return __request(OpenAPI, {
			method: 'GET',
			url: '/downloads/options',
			errors: {
				403: `Forbidden`
			}
		});
	}

	/**
	 * Get Download
	 * @returns Download Successful Response
	 * @throws ApiError
	 */
	public static getDownload(
		data: DownloadsData['payloads']['GetDownload']
	): CancelablePromise<DownloadsData['responses']['GetDownload']> {
		const { downloadId } = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/downloads/{download_id}',
			path: {
				download_id: downloadId
			},
			errors: {
				403: `Forbidden`,
				404: `Not Found`,
				422: `Validation Error`
			}
		});
	}

	/**
	 * Delete Download
	 * @returns void Successful Response
	 * @throws ApiError
	 */
	public static deleteDownload(
		data: DownloadsData['payloads']['DeleteDownload']
	): CancelablePromise<DownloadsData['responses']['DeleteDownload']> {
		const { downloadId } = data;
		return __request(OpenAPI, {
			method: 'DELETE',
			url: '/downloads/{download_id}',
			path: {
				download_id: downloadId
			},
			errors: {
				403: `Forbidden`,
				404: `Not Found`,
				422: `Validation Error`
			}
		});
	}

	/**
	 * Get Download File
	 * @returns binary Successful Response
	 * @throws ApiError
	 */
	public static getDownloadFile(
		data: DownloadsData['payloads']['GetDownloadFile']
	): CancelablePromise<DownloadsData['responses']['GetDownloadFile']> {
		const { downloadId } = data;
		return __request(OpenAPI, {
			method: 'GET',
			url: '/downloads/{download_id}/file',
			path: {
				download_id: downloadId
			},
			errors: {
				403: `Forbidden`,
				404: `Not Found`,
				422: `Validation Error`
			}
		});
	}
}
