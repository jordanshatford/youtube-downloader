/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { Session } from '../models/Session';

import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';

export class SessionService {

  /**
   * Get Session
   * @returns Session Successful Response
   * @throws ApiError
   */
  public static getSession(): CancelablePromise<Session> {
    return __request(OpenAPI, {
      method: 'GET',
      url: '/session',
    });
  }

  /**
   * Delete Session
   * @returns void
   * @throws ApiError
   */
  public static deleteSession(): CancelablePromise<void> {
    return __request(OpenAPI, {
      method: 'DELETE',
      url: '/session',
      errors: {
        403: `Forbidden`,
      },
    });
  }

  /**
   * Get Session Validate
   * @returns Session Successful Response
   * @throws ApiError
   */
  public static getSessionValidate(): CancelablePromise<Session> {
    return __request(OpenAPI, {
      method: 'GET',
      url: '/session/validate',
      errors: {
        403: `Forbidden`,
      },
    });
  }

}
