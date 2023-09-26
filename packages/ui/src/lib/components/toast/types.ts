import type { ToastVariants } from './Toast.svelte';

// Position of the toasts. This will also effect how the toasts stack.
export type ToastPosition =
	| 'top-left'
	| 'top-center'
	| 'top-right'
	| 'bottom-left'
	| 'bottom-center'
	| 'bottom-right';

// Variant of toast to display.
export type ToastVariant = ToastVariants['variant'];

// Life-cycle hooks run during various stages of the toast.
export interface ToastLifeCycles {
	// Run when the toast is added to the store.
	onMount?: () => void;
	// Run when the toast is removed from the store. Note: does not run when a toast is closed by user.
	onRemove?: () => void;
}

// Options passed to a toast function call.
export interface ToastFunctionOptions extends ToastLifeCycles {
	// Allows the toast to be closed manually.
	closable?: boolean;
	// Duration to show the toast.
	duration?: number;
	// If the toast should be shown infinitely.
	infinite?: boolean;
}

// Options used for content in the toast itself.
export interface ToastContentOptions {
	title: string;
	description: string;
}

// Options passed to the toast component.
export type ToastComponentOptions = Required<Omit<ToastFunctionOptions, 'onMount' | 'onRemove'>>;

// Values stored in the toasts store.
export interface ToastComponent extends ToastComponentOptions, ToastContentOptions {
	id: string;
	variant: ToastVariant;
}

// Options passed to a promise based toast.
export interface ToastPromiseOptions extends Partial<ToastFunctionOptions> {
	// The loading message of the promise.
	loading: ToastContentOptions;
	// The text to be displayed if the promise is resolved.
	success: ToastContentOptions;
	// The text to be displayed if the promise is rejected.
	error: ToastContentOptions;
	// Function the run when the promise has started.
	onStart?: () => void;
	// Function to run when the promise has been resolved.
	onSuccess?: <T = unknown>(data: T) => void;
	// Function to run when the promise has been rejected.
	onError?: <T = unknown>(data: T) => void;
	// Function to run when the promise has ended, no matter the result.
	onFinish?: () => void;
}

// The toast animation properties.
export interface ToastAnimation {
	// The starting scale size.
	start: number;
	// The starting opacity.
	opacity: number;
	// How long the toast animation is.
	duration: number;
}
