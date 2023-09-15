import {
	type IconSource,
	ExclamationCircleIcon,
	ExclamationTriangleIcon,
	CheckCircleIcon,
	InformationCircleIcon,
	LoaderIcon
} from './icons';

/**
 * Helper function used to attempt to provide icon based on some value
 * @param value some unknown value, could be string, number, boolean, etc
 * @returns IconSource or undefined
 */
export function toIcon(value: unknown, extras?: { loading?: boolean }): IconSource | undefined {
	if (extras?.loading) {
		return LoaderIcon;
	}
	switch (value) {
		case 'error':
			return ExclamationCircleIcon;
		case 'warning':
			return ExclamationTriangleIcon;
		case 'info':
			return InformationCircleIcon;
		case 'success':
			return CheckCircleIcon;
		case 'promise':
			return LoaderIcon;
		default:
			return undefined;
	}
}

/**
 * Helper function to check if running in browser
 * @returns true when running in browser, false otherwise
 */
export const browser = () => typeof window !== 'undefined';
