<script lang="ts" context="module">
	import {
		AlertCircleIcon,
		CheckCircleIcon,
		AlertTriangleIcon,
		LoaderIcon,
		InfoIcon
	} from '../../icons';
	export const ICONS_MAP: { readonly [T in ToastType]: typeof AlertCircleIcon } = {
		error: AlertCircleIcon,
		warning: AlertTriangleIcon,
		info: InfoIcon,
		success: CheckCircleIcon,
		promise: LoaderIcon
	};
</script>

<script lang="ts">
	import type { ToastType } from './types';
	import { toast as _toast, position } from './stores';
	import type { ToastComponent } from './types';
	import { XIcon } from '../../icons';
	export let toast: ToastComponent;
</script>

<div
	id="yd-toast-{toast.id}"
	class="yd-toast {toast.type}"
	data-position={$position}
	aria-live="polite"
	role="status"
>
	<div class="yd-toast-bar" />
	<div class="yd-toast-icon {toast.type}">
		<svelte:component this={ICONS_MAP[toast.type]} size="1.5x" />
	</div>
	<div class="yd-toast-message">
		{toast.message}
	</div>
	{#if toast.closable && toast.type !== 'promise'}
		<button type="button" class="yd-toast-dismiss" on:click={() => _toast.remove(toast.id)}>
			<XIcon size="1x" />
		</button>
	{/if}
</div>

<style>
	.yd-toast {
		background: var(--yd-toast-bg, #333);
		color: var(--yd-toast-text, #fff);
		padding: var(--yd-toast-padding, 12px 15px 12px 18px);
		border-radius: var(--yd-toast-radius, 4px);
		box-shadow: var(--yd-toast-shadow, 0 2px 7px rgba(0, 0, 0, 0.25));
		font-size: var(--yd-toast-font-size, 14px);
		position: relative;
		overflow: hidden;
		pointer-events: all;
		display: flex;
		gap: var(--yd-toast-dismiss-gap, 8px);
		max-width: var(--yd-toast-max-width, unset);
	}
	.yd-toast-bar {
		position: absolute;
		top: 0;
		left: 0;
		width: var(--yd-toast-bar-width, 3px);
		height: 100%;
		background: var(--yd-toast-colour);
	}
	.yd-toast-icon {
		min-width: var(--yd-toast-icon-size, 21px);
		min-height: var(--yd-toast-icon-size, 21px);
		max-width: var(--yd-toast-icon-size, 21px);
		max-height: var(--yd-toast-icon-size, 21px);
		color: var(--yd-toast-colour);
	}
	.yd-toast-icon.promise {
		animation: promiseSpin 1s linear infinite;
	}
	.yd-toast-dismiss {
		min-width: var(--yd-toast-icon-size, 21px);
		min-height: var(--yd-toast-icon-size, 21px);
		max-width: var(--yd-toast-icon-size, 21px);
		max-height: var(--yd-toast-icon-size, 21px);
		padding: var(--yd-toast-icon-padding, 2px);
	}
	.yd-toast.info {
		--yd-toast-colour: var(--yd-toast-info-colour, #38bdf8);
	}
	.yd-toast.success {
		--yd-toast-colour: var(--yd-toast-success-colour, #4ade80);
	}
	.yd-toast.warning {
		--yd-toast-colour: var(--yd-toast-warning-colour, #fb923c);
	}
	.yd-toast.error {
		--yd-toast-colour: var(--yd-toast-error-colour, #ef4444);
	}
	@keyframes promiseSpin {
		from {
			rotate: 0deg;
		}
		to {
			rotate: 360deg;
		}
	}
</style>
