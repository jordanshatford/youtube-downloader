import { writable, get } from 'svelte/store';
import { DEFAULT_OPTIONS, DEFAULT_POSITION } from './utils';
import { browser } from '../../utilities';

import type {
	ToastFunction,
	ToastVariant,
	ToastPosition,
	ToastComponent,
	ToastPromiseFunction,
	ToastAddOptions
} from './types';

const TOASTS = writable<ToastComponent[]>([]);

function addToast(
	variant: ToastVariant,
	title: string,
	description: string,
	{ opts, id }: ToastAddOptions
) {
	const uuid = id ?? crypto.randomUUID();

	const { closable, duration, infinite, onMount, onRemove } = { ...DEFAULT_OPTIONS, ...opts };

	const props: ToastComponent = {
		id: uuid,
		variant,
		title,
		description,
		duration,
		closable,
		infinite
	};

	if (browser()) onMount?.();

	upsert(props, uuid);

	if (!infinite && variant !== 'promise') {
		setTimeout(() => {
			remove(uuid);
			onRemove?.();
		}, duration);
	}

	return uuid;
}

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
	if (get(TOASTS).some((el) => el.id === id))
		TOASTS.update((toasts) => toasts.filter((toast) => toast.id !== id));
};
const clear = () => {
	TOASTS.set([]);
};

const info: ToastFunction = (title, description, opts = DEFAULT_OPTIONS) =>
	addToast('info', title, description, { opts });
const success: ToastFunction = (title, description, opts = DEFAULT_OPTIONS) =>
	addToast('success', title, description, { opts });
const warning: ToastFunction = (title, description, opts = DEFAULT_OPTIONS) =>
	addToast('warning', title, description, { opts });
const error: ToastFunction = (title, description, opts = DEFAULT_OPTIONS) =>
	addToast('error', title, description, { opts });
const promise: ToastPromiseFunction<unknown> = (promise, opts) => {
	if (promise instanceof Promise === false) throw Error('`promise` is not a valid Promise.');

	const id = addToast('promise', opts.loading.title, opts.loading.description, { opts });

	opts?.onStart?.();

	promise
		.then((data) => {
			addToast('success', opts.success.title, opts.success.description, { opts, id });
			opts?.onSuccess?.(data);
		})
		.catch((err) => {
			addToast('error', opts.error.title, opts.error.description, { opts, id });
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

const createToastStore = () => {
	const { subscribe } = TOASTS;
	return {
		// Add an information toast.
		info,
		// Add a success toast.
		success,
		// Add a warning toast.
		warning,
		// Add an error toast.
		error,
		// Add a promise chain toast.
		promise,
		// Remove a single toast based on the ID passed.
		remove,
		// Remove all toasts.
		clear,
		subscribe
	};
};

export const toast = createToastStore();

export const position = writable<ToastPosition>(DEFAULT_POSITION);
