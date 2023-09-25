import type { ToastComponentOptions, ToastAnimation, ToastPosition } from './types';

/**
 * The default position for all toasts
 */
export const DEFAULT_POSITION: ToastPosition = 'bottom-right';

/**
 * The default options for the toasts.
 */
export const DEFAULT_OPTIONS: ToastComponentOptions = {
	closable: true,
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
