import type { ApiRequestOptions } from './generated/core/ApiRequestOptions';
import { resolve } from './generated/core/request';
import { type DownloadStatusUpdate, OpenAPI } from './generated';

type EventSourceHandler<T> = (event: T) => void;

// Options used when getting information to setup the EventSource. This
// is not actually a GET request.
const options: ApiRequestOptions = {
	method: 'GET',
	url: '/downloads/status'
};

export class DownloadsStatusService {
	public static async setup(
		onMessage?: EventSourceHandler<DownloadStatusUpdate>,
		onError?: EventSourceHandler<Event>,
		onOpen?: EventSourceHandler<Event>
	): Promise<void> {
		// Get token from OpenAPI set by user previously. This works in the
		// same way as the generated code. This token is passed as a session_id
		// query parameter to the endpoint as it cannot be passed in the header.
		const sessionId = await resolve(options, OpenAPI.TOKEN);
		const url = `${OpenAPI.BASE}${options.url}?session_id=${sessionId}`;
		const source = new EventSource(url);
		// Parse message data before callback.
		source.onmessage = (event: MessageEvent) => {
			const data = JSON.parse(event.data) as DownloadStatusUpdate;
			onMessage?.(data);
		};
		// Forward onerror and onopen messages incase user wants to use them.
		source.onerror = (event) => onError?.(event);
		source.onopen = (event) => onOpen?.(event);
	}
}
