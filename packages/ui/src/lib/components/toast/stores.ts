import { writable, get } from 'svelte/store';
import { DEFAULT_OPTIONS, DEFAULT_POSITION } from './utils';
import { browser } from '../../utilities';

import type {
	ToastVariant,
	ToastPosition,
	ToastComponent,
	ToastComponentOptions,
	ToastFunctionOptions,
	ToastPromiseOptions
} from './types';

const TOASTS = writable<ToastComponent[]>([]);

function addToast(
	variant: ToastVariant,
	title: string,
	description: string,
	{ opts, id }: { opts?: ToastFunctionOptions; id?: string }
) {
	const uuid = id ?? crypto.randomUUID();

	const { closable, duration, infinite, onMount, onRemove } = { ...get(options), ...opts };

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

function upsert(props: ToastComponent, id: string) {
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
}

function remove(id: string) {
	if (get(TOASTS).some((el) => el.id === id))
		TOASTS.update((toasts) => toasts.filter((toast) => toast.id !== id));
}

function clear() {
	TOASTS.set([]);
}

function info(title: string, description: string, opts: ToastFunctionOptions = get(options)) {
	addToast('info', title, description, { opts });
}

function success(title: string, description: string, opts: ToastFunctionOptions = get(options)) {
	addToast('success', title, description, { opts });
}

function warning(title: string, description: string, opts: ToastFunctionOptions = get(options)) {
	addToast('warning', title, description, { opts });
}

function error(title: string, description: string, opts: ToastFunctionOptions = get(options)) {
	addToast('error', title, description, { opts });
}

function promise<T>(promise: Promise<T>, opts: ToastPromiseOptions) {
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
				setTimeout(
					() => {
						remove(id);
					},
					opts.duration ?? get(options).duration
				);
			}
			opts?.onFinish?.();
		});
}

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

export const options = writable<ToastComponentOptions>(DEFAULT_OPTIONS);
