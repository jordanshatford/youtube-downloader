<script lang="ts" module>
	import { tv } from 'tailwind-variants';

	const paginationClasses = tv({
		slots: {
			containerClass: 'flex justify-center gap-1 text-xs font-medium',
			outerButtonClass:
				'inline-flex h-8 w-8 items-center justify-center rounded-sm border border-zinc-200 bg-white hover:bg-zinc-50 text-zinc-900 dark:border-zinc-800 dark:bg-zinc-900 dark:hover:bg-zinc-800 dark:text-white',
			outerButtonIconClass: 'h-3 w-3',
			numberButtonClass: 'block h-8 w-8 rounded-sm border text-center leading-8'
		},
		variants: {
			active: {
				true: {
					numberButtonClass:
						'border-blue-600 bg-blue-600 text-white dark:text-white hover:bg-blue-500'
				},
				false: {
					numberButtonClass:
						'border-zinc-100 bg-white text-zinc-900 dark:border-zinc-800 dark:bg-zinc-900 dark:text-white hover:bg-zinc-50 dark:hover:bg-zinc-800'
				}
			}
		}
	});
</script>

<script lang="ts">
	import { ChevronLeftIcon, ChevronRightIcon, Icon } from '../icons';

	interface Props {
		class?: string;
		page: number;
		totalPages?: number;
		clickableNumbersAroundPage?: number;
	}

	let {
		class: className = '',
		page = $bindable(),
		totalPages = 1,
		clickableNumbersAroundPage = 3
	}: Props = $props();

	// Get start and end values of clickable numbers
	let clickableFirstNumber = $derived(Math.max(page - clickableNumbersAroundPage, 1));
	let clickableLastNumber = $derived(Math.min(page + clickableNumbersAroundPage, totalPages));

	// Create array of values between clickableFirstNumber and clickableLastNumber
	function toRangeArray(start: number, end: number): number[] {
		return Array.from({ length: end - start + 1 }, (_v, index) => index + start);
	}
	let clickableNumbers = $derived(toRangeArray(clickableFirstNumber, clickableLastNumber));

	const { containerClass, outerButtonClass, outerButtonIconClass, numberButtonClass } =
		paginationClasses();
</script>

<ol class={containerClass({ class: className })}>
	<li>
		<button onclick={() => (page = Math.max(page - 1, 1))} class={outerButtonClass()}>
			<span class="sr-only">Prev Page</span>
			<Icon src={ChevronLeftIcon} theme="solid" class={outerButtonIconClass()} />
		</button>
	</li>
	{#each clickableNumbers as n}
		<li>
			<button onclick={() => (page = n)} class={numberButtonClass({ active: page == n })}>
				{n}
			</button>
		</li>
	{/each}
	<li>
		<button onclick={() => (page = Math.min(page + 1, totalPages))} class={outerButtonClass()}>
			<span class="sr-only">Next Page</span>
			<Icon src={ChevronRightIcon} theme="solid" class={outerButtonIconClass()} />
		</button>
	</li>
</ol>
