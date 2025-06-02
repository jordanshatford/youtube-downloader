import type {
	ToastComponent,
	ToastComponentOptions,
	ToastFunctionOptions,
	ToastPosition,
	ToastPromiseOptions,
	ToastVariant
} from './types';
import { browser } from '../../utilities';
import { DEFAULT_OPTIONS, DEFAULT_POSITION } from './utils';

class ToastStore {
	public toasts = $state<ToastComponent[]>([]);
	public position = $state<ToastPosition>(DEFAULT_POSITION);
	public options = $state<ToastComponentOptions>(DEFAULT_OPTIONS);

	public info(title: string, description: string, opts: ToastFunctionOptions = this.options) {
		this.addToast('info', title, description, { opts });
	}

	public success(title: string, description: string, opts: ToastFunctionOptions = this.options) {
		this.addToast('success', title, description, { opts });
	}

	public warning(title: string, description: string, opts: ToastFunctionOptions = this.options) {
		this.addToast('warning', title, description, { opts });
	}

	public error(title: string, description: string, opts: ToastFunctionOptions = this.options) {
		this.addToast('error', title, description, { opts });
	}

	public promise<T>(promise: Promise<T>, opts: ToastPromiseOptions) {
		if (promise instanceof Promise === false) throw Error('`promise` is not a valid Promise.');

		const id = this.addToast('promise', opts.loading.title, opts.loading.description, {
			opts
		});

		opts?.onStart?.();

		promise
			.then((data) => {
				this.addToast('success', opts.success.title, opts.success.description, {
					opts,
					id
				});
				opts?.onSuccess?.(data);
			})
			.catch((err) => {
				this.addToast('error', opts.error.title, opts.error.description, {
					opts,
					id
				});
				opts?.onError?.(err);
			})
			.finally(() => {
				if (!opts?.infinite) {
					setTimeout(() => {
						this.remove(id);
					}, opts.duration ?? this.options.duration);
				}
				opts?.onFinish?.();
			});
	}

	public remove(id: string) {
		if (this.toasts.some((el) => el.id === id))
			this.toasts = this.toasts.filter((toast) => toast.id !== id);
	}

	public clear() {
		this.toasts = [];
	}

	private addToast(
		variant: ToastVariant,
		title: string,
		description: string,
		{ opts, id }: { opts?: ToastFunctionOptions; id?: string }
	) {
		const uuid = id ?? crypto.randomUUID();

		const { closable, duration, infinite, onMount, onRemove } = {
			...this.options,
			...opts
		};

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

		this.upsert(props, uuid);

		if (!infinite && variant !== 'promise') {
			setTimeout(() => {
				this.remove(uuid);
				onRemove?.();
			}, duration);
		}

		return uuid;
	}

	private upsert(props: ToastComponent, id: string) {
		if (this.toasts.find((toast) => toast.id === id)) {
			this.toasts = this.toasts.map((toast) => {
				if (toast.id === id) return { ...toast, ...props };
				return toast;
			});
		} else {
			this.toasts = this.position.includes('bottom')
				? [...this.toasts, props]
				: [props, ...this.toasts];
		}
	}
}

export const toasts = new ToastStore();
