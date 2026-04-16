/**
 * Creates a debounced function that delays invoking `fn` until after
 * `delay` milliseconds have elapsed since the last time it was called.
 *
 * @template T - The type of the function being debounced.
 * @param fn - The function to debounce.
 * @param delay - The delay in milliseconds (default: 300).
 * @returns A debounced version of the provided function.
 */
export function debounce<T extends (...args: unknown[]) => void>(fn: T, delay = 300) {
	let timeout: ReturnType<typeof setTimeout>;

	return (...args: Parameters<T>) => {
		clearTimeout(timeout);
		timeout = setTimeout(() => {
			fn(...args);
		}, delay);
	};
}
