import type { AvailableDownloadOptions, Download, DownloadInput } from '../models';
import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';

export type TDataPutDownloads = {
	requestBody: DownloadInput;
};
export type TDataPostDownloads = {
	requestBody: DownloadInput;
};
export type TDataGetDownload = {
	downloadId: string;
};
export type TDataDeleteDownload = {
	downloadId: string;
};
export type TDataGetDownloadFile = {
	downloadId: string;
};

export class DownloadsService {
	/**
	 * Get Downloads
	 * @returns Download Successful Response
	 * @throws ApiError
	 */
	public static getDownloads(): CancelablePromise<Array<Download>> {
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
	public static putDownloads(data: TDataPutDownloads): CancelablePromise<Download> {
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
	public static postDownloads(data: TDataPostDownloads): CancelablePromise<Download> {
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
	public static getDownloadsOptions(): CancelablePromise<AvailableDownloadOptions> {
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
	public static getDownload(data: TDataGetDownload): CancelablePromise<Download> {
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
	public static deleteDownload(data: TDataDeleteDownload): CancelablePromise<void> {
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
	public static getDownloadFile(data: TDataGetDownloadFile): CancelablePromise<Blob | File> {
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
