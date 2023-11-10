/**
 * Check if a url is for a YouTube video.
 * @param url - string | URL
 * @returns boolean
 */
export function isYouTubeVideo(url: string | URL): boolean {
	const m =
		/^(?:https?:\/\/)?(?:www\.)?(?:youtu\.be\/|youtube\.com\/(?:embed\/|v\/|watch\?v=|watch\?.+&v=))((\w|-){11})(?:\S+)?$/;
	return url.toString().match(m) ? true : false;
}
