import type { Component } from 'svelte';
import { AlertCircleIcon, CheckCircleIcon, SpinnerIcon } from '$uilib';

import type { DownloadState, DownloadStatus } from '@yd/client';

const STATE_CLASS_LOOKUP: Record<DownloadState, string> = {
	WAITING: 'bg-yellow-100 text-yellow-700 dark:bg-yellow-700 dark:text-yellow-100',
	DOWNLOADING: 'bg-blue-100 text-blue-700 dark:bg-blue-700 dark:text-blue-100',
	PROCESSING: 'bg-purple-100 text-purple-700 dark:bg-purple-700 dark:text-purple-100',
	ERROR: 'bg-red-100 text-red-700 dark:bg-red-700 dark:text-red-100',
	DONE: 'bg-emerald-100 text-emerald-700 dark:bg-emerald-700 dark:text-emerald-100'
};

/**
 * Convert a download state into a corresponding class string for styling purposes.
 * @param state - the download state to convert into a class string.
 * @returns a string representing the CSS classes associated with the given download state.
 */
export function toClassFromState(state: DownloadState): string {
	return STATE_CLASS_LOOKUP[state];
}

const STATE_CLASS_LOOKUP_NEW: Record<DownloadState, string> = {
	WAITING: 'text-yellow-500',
	DOWNLOADING: 'text-blue-500',
	PROCESSING: 'text-purple-500',
	ERROR: 'text-red-500',
	DONE: 'text-emerald-500'
};

/**
 * Convert a download state into a corresponding class string for styling purposes.
 * @param state - the download state to convert into a class string.
 * @returns a string representing the CSS classes associated with the given download state.
 */
export function toClassFromStateNew(state: DownloadState): string {
	return STATE_CLASS_LOOKUP_NEW[state];
}

const STATE_ICON_LOOKUP: Record<DownloadState, Component> = {
	WAITING: SpinnerIcon,
	DOWNLOADING: SpinnerIcon,
	PROCESSING: SpinnerIcon,
	ERROR: AlertCircleIcon,
	DONE: CheckCircleIcon
};

/**
 * Convert a download state into a corresponding icon component for visual representation.
 * @param state - the download state to convert into an icon component.
 * @returns a Svelte component representing the icon associated with the given download state.
 */
export function toIconFromState(state: DownloadState): Component {
	return STATE_ICON_LOOKUP[state];
}

const PP_LOOKUP: Record<string, string> = {
	extractaudio: 'Extracting Audio',
	videoconvertor: 'Converting Video',
	metadata: 'Embedding Metadata',
	embedthumbnail: 'Embedding Thumbnail',
	embedsubtitle: 'Embedding Subtitle',
	movefiles: 'Finalizing'
};

const STATE_TEXT_LOOKUP: Record<DownloadState, string> = {
	WAITING: 'Waiting',
	DOWNLOADING: 'Downloading',
	PROCESSING: 'Processing',
	ERROR: 'Error',
	DONE: 'Done'
};

/**
 * Convert a download status into a corresponding text string for visual representation.
 * @param status - the download status to convert into text.
 * @returns a string representing the text to display for the status.
 */
export function toTextFromStatus(status: DownloadStatus): string {
	const fallback = STATE_TEXT_LOOKUP[status.state] || status.state;
	if (status.postprocessor) {
		return PP_LOOKUP[status.postprocessor?.toLowerCase()] ?? fallback;
	}
	return fallback;
}
