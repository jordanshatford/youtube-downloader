/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { AvailableDownloadOptions } from '../models/AvailableDownloadOptions';
import type { Download } from '../models/Download';

import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';

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
        403: `Forbidden`,
      },
    });
  }

  /**
   * Put Downloads
   * @param requestBody
   * @returns Download Successful Response
   * @throws ApiError
   */
  public static putDownloads(
    requestBody: Download,
  ): CancelablePromise<Download> {
    return __request(OpenAPI, {
      method: 'PUT',
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
   * Post Downloads
   * @param requestBody
   * @returns Download Successful Response
   * @throws ApiError
   */
  public static postDownloads(
    requestBody: Download,
  ): CancelablePromise<Download> {
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
   * Get Downloads Options
   * @returns AvailableDownloadOptions Successful Response
   * @throws ApiError
   */
  public static getDownloadsOptions(): CancelablePromise<AvailableDownloadOptions> {
    return __request(OpenAPI, {
      method: 'GET',
      url: '/downloads/options',
      errors: {
        403: `Forbidden`,
      },
    });
  }

  /**
   * Get Download
   * @param downloadId
   * @returns Download Successful Response
   * @throws ApiError
   */
  public static getDownload(
    downloadId: string,
  ): CancelablePromise<Download> {
    return __request(OpenAPI, {
      method: 'GET',
      url: '/downloads/{download_id}',
      path: {
        'download_id': downloadId,
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
   * @param downloadId
   * @returns void
   * @throws ApiError
   */
  public static deleteDownload(
    downloadId: string,
  ): CancelablePromise<void> {
    return __request(OpenAPI, {
      method: 'DELETE',
      url: '/downloads/{download_id}',
      path: {
        'download_id': downloadId,
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
   * @param downloadId
   * @returns binary Successful Response
   * @throws ApiError
   */
  public static getDownloadFile(
    downloadId: string,
  ): CancelablePromise<Blob> {
    return __request(OpenAPI, {
      method: 'GET',
      url: '/downloads/{download_id}/file',
      path: {
        'download_id': downloadId,
      },
      errors: {
        403: `Forbidden`,
        404: `Not Found`,
        422: `Validation Error`,
      },
    });
  }

}
