import type { Video } from '../models/Video';
import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';

export type TDataGetSearch = {
	query: string;
};
export type TDataGetVideo = {
	id: string;
};

export class SearchService {
	/**
	 * Get Search
	 * @returns Video Successful Response
	 * @throws ApiError
	 */
	public static getSearch(data: TDataGetSearch): CancelablePromise<Array<Video>> {
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
	public static getNextSearch(): CancelablePromise<Array<Video>> {
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
	public static getVideo(data: TDataGetVideo): CancelablePromise<Video> {
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
