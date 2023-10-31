/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */

import type { DownloadState } from './DownloadState';

export type DownloadStatus = {
  state: DownloadState;
  downloaded_bytes?: (number | null);
  total_bytes?: (number | null);
  progress?: (number | null);
  elapsed?: (number | null);
  eta?: (number | null);
  speed?: (number | null);
  postprocessor?: (string | null);
};

