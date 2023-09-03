import type { ToastComponentOptions, ToastAnimation } from './types';

/**
 * The default options for the toasts.
 */
export const DEFAULT_OPTIONS: ToastComponentOptions = {
	closable: false,
	duration: 5000,
	infinite: false
};

/**
 * Default animation for the toasts.
 */
export const DEFAULT_ANIMATION: ToastAnimation = {
	start: 0.75,
	opacity: 0,
	duration: 150
};

/**
 * Shallow merges two objects while replacing the same keys.
 * @param original The original object to be overwritten.
 * @param newObject The object to be added to the original object, replacing existing keys.
 */
export const objectMerge = <TOriginal extends object, TNew extends object | undefined>(
	original: TOriginal,
	newObject: TNew
): TOriginal & TNew => {
	return {
		...original,
		...newObject
	};
};
