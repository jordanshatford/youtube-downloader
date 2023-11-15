import { defineExtensionMessaging, GetDataType } from '@webext-core/messaging';
import { Download, DownloadOptions, Session, Video } from '@yd/client';

/**
 * This file represents all messenging that happens across the various
 * parts of the extension. This allows each (popup, background, content)
 * script(s) to communicate with each other in a typesafe manner.
 */
interface MessagingMap {
	// Called when a new session is created.
	NewSession: (session: Session) => void;
	// Called when a new video is the most relevant one.
	VideoChanged: (video?: Video) => void;
	// Called when settings are changed.
	SettingsChanged: (settings: DownloadOptions) => void;
	// Called when a download is started for a given video.
	DownloadStart: (download: Download) => void;
	// Called when a status update was detected from the backend.
	StatusUpdate: (update: Download) => void;
	// Called when a download has been completed and file is on computer.
	DownloadDone: (download: Download) => void;
}

export const { sendMessage, onMessage } = defineExtensionMessaging<MessagingMap>();

/**
 * Helper function wrapping the send message function but ignoring any errors or return values.
 * This works similarly to SSE where we send and forget. If someone is listening they will get the
 * update, otherwise we dont really care.
 */
export async function sendMessageIgnoreReturn<TType extends keyof MessagingMap>(
	type: TType,
	data: GetDataType<MessagingMap[TType]>,
	tabId?: number | undefined
): Promise<void> {
	try {
		await sendMessage(type, data, tabId);
	} catch (e) {
		// Ignore possible error when attempting to send the message.
	}
}
