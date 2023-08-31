/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */

import type { DownloadState } from './DownloadState';

export type DownloadStatusUpdate = {
  state: DownloadState;
  progress?: (number | null);
  eta?: (number | null);
  id: string;
};

