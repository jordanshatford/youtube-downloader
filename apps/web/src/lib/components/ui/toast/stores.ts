import { writable, get } from 'svelte/store';
import { DEFAULT_OPTIONS, objectMerge } from './utils';

import type {
	ToastFunction,
	ToastType,
	ToastPosition,
	ToastFunctionOptions,
	ToastComponent,
	ToastPromiseFunction,
	ToastAddOptions
} from './types';

const TOASTS = writable<ToastComponent[]>([]);

const addToast = (type: ToastType, message: string, { opts, id }: ToastAddOptions) => {
	const uuid = id || crypto.randomUUID();

	const { closable, infinite, onMount, onRemove, duration } = objectMerge(
		DEFAULT_OPTIONS,
		opts
	) as Required<ToastFunctionOptions>;

	const props: ToastComponent = {
		id: uuid,
		type,
		message,
		duration,
		closable,
		infinite
	};

	if (typeof window !== 'undefined') onMount?.();

	upsert(props, uuid);

	if (!infinite && type !== 'promise') {
		setTimeout(() => {
			remove(uuid);
			onRemove?.();
		}, duration);
	}

	return uuid;
};

const upsert = (props: ToastComponent, id: string) => {
	if (get(TOASTS).find((toast) => toast.id === id)) {
		TOASTS.update((toasts) => {
			return toasts.map((toast) => {
				if (toast.id === id) return { ...toast, ...props };
				return toast;
			});
		});
	} else {
		TOASTS.update(
			(toasts) =>
				(toasts = get(position).includes('bottom') ? [...toasts, props] : [props, ...toasts])
		);
	}
};
const remove = (id: string) => {
	if (get(TOASTS).find((el) => el.id === id))
		TOASTS.update((toasts) => toasts.filter((toast) => toast.id !== id));
};
const clear = () => {
	TOASTS.set([]);
};

const info: ToastFunction = (message, opts = DEFAULT_OPTIONS) =>
	addToast('info', message, { opts });
const success: ToastFunction = (message, opts = DEFAULT_OPTIONS) =>
	addToast('success', message, { opts });
const warning: ToastFunction = (message, opts = DEFAULT_OPTIONS) =>
	addToast('warning', message, { opts });
const error: ToastFunction = (message, opts = DEFAULT_OPTIONS) =>
	addToast('error', message, { opts });
const promise: ToastPromiseFunction<unknown> = (promise, opts) => {
	if (promise instanceof Promise === false) throw Error('`promise` is not a valid Promise.');

	const id = addToast('promise', opts.loading, { opts });

	opts?.onStart?.();

	promise
		.then((data) => {
			addToast('success', opts.success, { opts, id });
			opts?.onSuccess?.(data);
		})
		.catch((err) => {
			addToast('error', opts.error, { opts, id });
			opts?.onError?.(err);
		})
		.finally(() => {
			if (!opts?.infinite) {
				setTimeout(() => {
					remove(id);
				}, opts.duration || DEFAULT_OPTIONS.duration);
			}
			opts?.onFinish?.();
		});
};

const createStore = () => {
	const { subscribe } = TOASTS;

	return {
		/**
		 * Add a info type toast.\
		 * Usually indicates information to the user, but isn’t important.
		 * @param message The message to be displayed in the toast.
		 * @param opts Options for the toast.
		 */
		info,
		/**
		 * Add a success type toast.\
		 * Indicates to the user something good has happened.
		 * @param message The message to be displayed in the toast.
		 * @param opts Options for the toast.
		 */
		success,
		/**
		 * Add a warning type toast.\
		 * Tell the user something may be wrong but isn’t critical.
		 * @param message The message to be displayed in the toast.
		 * @param opts Options for the toast.
		 */
		warning,
		/**
		 * Add an error type toast.\
		 * Alert the user something critical has happened.
		 * @param message The message to be displayed in the toast.
		 * @param opts Options for the toast.
		 */
		error,
		/**
		 * Add a promise toast chain.\
		 * Indicates to the user that something is happening in the background.
		 * @param promise The promise to be used.
		 * @param opts Options for the promise chain.
		 */
		promise,
		/**
		 * Remove a toast based on the unique ID.
		 * @param id The unique ID of the toast.
		 */
		remove,
		/**
		 * Removes all toasts.
		 */
		clear,
		subscribe
	};
};

export const toast = createStore();

export const position = writable<ToastPosition>('bottom-left');
