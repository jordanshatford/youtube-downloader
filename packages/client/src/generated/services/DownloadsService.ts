/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { DownloadStatusUpdate } from '../models/DownloadStatusUpdate';
import type { VideoWithOptions } from '../models/VideoWithOptions';
import type { VideoWithOptionsAndStatus } from '../models/VideoWithOptionsAndStatus';

import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';

export class DownloadsService {

  /**
   * Get Downloads
   * @returns VideoWithOptionsAndStatus Successful Response
   * @throws ApiError
   */
  public static getDownloads(): CancelablePromise<Array<VideoWithOptionsAndStatus>> {
    return __request(OpenAPI, {
      method: 'GET',
      url: '/downloads',
      errors: {
        403: `Forbidden`,
      },
    });
  }

  /**
   * Post Downloads
   * @param requestBody
   * @returns VideoWithOptions Successful Response
   * @throws ApiError
   */
  public static postDownloads(
    requestBody: VideoWithOptions,
  ): CancelablePromise<VideoWithOptions> {
    return __request(OpenAPI, {
      method: 'POST',
      url: '/downloads',
      body: requestBody,
      mediaType: 'application/json',
      errors: {
        403: `Forbidden`,
        422: `Validation Error`,
      },
    });
  }

  /**
   * Get Download
   * @param videoId
   * @returns VideoWithOptions Successful Response
   * @throws ApiError
   */
  public static getDownload(
    videoId: string,
  ): CancelablePromise<VideoWithOptions> {
    return __request(OpenAPI, {
      method: 'GET',
      url: '/downloads/{video_id}',
      path: {
        'video_id': videoId,
      },
      errors: {
        403: `Forbidden`,
        404: `Not Found`,
        422: `Validation Error`,
      },
    });
  }

  /**
   * Delete Download
   * @param videoId
   * @returns void
   * @throws ApiError
   */
  public static deleteDownload(
    videoId: string,
  ): CancelablePromise<void> {
    return __request(OpenAPI, {
      method: 'DELETE',
      url: '/downloads/{video_id}',
      path: {
        'video_id': videoId,
      },
      errors: {
        403: `Forbidden`,
        404: `Not Found`,
        422: `Validation Error`,
      },
    });
  }

  /**
   * Get Download File
   * @param videoId
   * @returns binary Successful Response
   * @throws ApiError
   */
  public static getDownloadFile(
    videoId: string,
  ): CancelablePromise<Blob> {
    return __request(OpenAPI, {
      method: 'GET',
      url: '/downloads/{video_id}/file',
      path: {
        'video_id': videoId,
      },
      errors: {
        403: `Forbidden`,
        404: `Not Found`,
        422: `Validation Error`,
      },
    });
  }

  /**
   * Get Download Status
   * @param videoId
   * @returns DownloadStatusUpdate Successful Response
   * @throws ApiError
   */
  public static getDownloadStatus(
    videoId: string,
  ): CancelablePromise<DownloadStatusUpdate> {
    return __request(OpenAPI, {
      method: 'GET',
      url: '/downloads/{video_id}/status',
      path: {
        'video_id': videoId,
      },
      errors: {
        403: `Forbidden`,
        404: `Not Found`,
        422: `Validation Error`,
      },
    });
  }

}
