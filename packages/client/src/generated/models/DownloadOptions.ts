/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { AudioFormat } from './AudioFormat';
import type { DownloadQuality } from './DownloadQuality';
import type { VideoFormat } from './VideoFormat';
export type DownloadOptions = {
  format: (AudioFormat | VideoFormat);
  quality: DownloadQuality;
  embed_metadata: boolean;
  embed_thumbnail: boolean;
  embed_subtitles: boolean;
};

