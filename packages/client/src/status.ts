import type { Download } from './generated/index';
import { client } from './generated/index';

type EventSourceHandler<T> = (event: T) => void;

export async function getDownloadsStatus(
	sessionId: string | (() => Promise<string> | string),
	callbacks: {
		onMessage?: EventSourceHandler<Download>;
		onError?: EventSourceHandler<Event>;
		onOpen?: EventSourceHandler<Event>;
	}
): Promise<EventSource> {
	const config = client.getConfig();
	const s = typeof sessionId === 'string' ? sessionId : await sessionId();
	const url = `${config.baseUrl}/downloads/status?session_id=${s}`;
	const source = new EventSource(url);
	// Parse message data before callback.
	source.onmessage = (event: MessageEvent) => {
		const data = JSON.parse(event.data) as Download;
		callbacks.onMessage?.(data);
	};
	// Forward onerror and onopen messages incase user wants to use them.
	source.onerror = (event) => callbacks.onError?.(event);
	source.onopen = (event) => callbacks.onOpen?.(event);
	return source;
}
