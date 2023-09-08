/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */

import type { Channel } from './Channel';
import type { DownloadOptions } from './DownloadOptions';
import type { DownloadStatus } from './DownloadStatus';

export type VideoWithOptionsAndStatus = {
  id: string;
  url: string;
  title: string;
  duration: string;
  thumbnail: string;
  channel: Channel;
  options: DownloadOptions;
  status: DownloadStatus;
};

