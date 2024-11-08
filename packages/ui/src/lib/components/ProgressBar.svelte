<script lang="ts" module>
	import type { VariantProps } from 'tailwind-variants';
	import { tv } from 'tailwind-variants';

	const progressBarClasses = tv({
		slots: {
			wrapperDivClass: 'relative',
			labelSpanClass:
				'absolute bottom-full mb-2 -translate-x-1/2 rounded-md border border-zinc-50 dark:border-zinc-600 bg-white dark:bg-zinc-800 px-2 py-1 text-sm text-zinc-600 dark:text-zinc-300 shadow',
			barDivClass:
				'relative flex h-2 w-full overflow-hidden rounded-full bg-zinc-200 dark:bg-zinc-700',
			progressDivClass: 'flex h-full items-center justify-center text-xs text-white'
		},
		variants: {
			variant: {
				error: {
					progressDivClass: 'bg-red-500'
				},
				warning: {
					progressDivClass: 'bg-yellow-500'
				},
				info: {
					progressDivClass: 'bg-blue-500'
				},
				success: {
					progressDivClass: 'bg-emerald-500'
				}
			}
		},
		defaultVariants: {
			variant: 'info'
		}
	});

	export type ProgressBarVariants = VariantProps<typeof progressBarClasses>;
</script>

<script lang="ts">
	export let value: number = 0;
	export let min: number = 0;
	export let max: number = 100;

	export let variant: ProgressBarVariants['variant'] = 'info';
	export let showLabel: boolean = false;

	$: percentage = ((value - min) / (max - min)) * 100;

	const { wrapperDivClass, labelSpanClass, barDivClass, progressDivClass } = progressBarClasses({
		variant
	});
</script>

<div {...$$restProps} class:mt-5={showLabel} class={$$props.class}>
	<div class={wrapperDivClass()}>
		{#if showLabel}
			<span class={labelSpanClass()} style="left: {percentage}%">{percentage}%</span>
		{/if}
		<div class={barDivClass()}>
			<div
				role="progressbar"
				aria-valuenow={value}
				aria-valuemin={min}
				aria-valuemax={max}
				style="width: {percentage}%"
				class={progressDivClass()}
			></div>
		</div>
	</div>
</div>
