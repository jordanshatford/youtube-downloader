<script lang="ts" context="module">
	import { tv } from 'tailwind-variants';

	const paginationClasses = tv({
		slots: {
			containerClass: 'flex justify-center gap-1 text-xs font-medium',
			outerButtonClass:
				'inline-flex h-8 w-8 items-center justify-center rounded border border-zinc-200 bg-white hover:bg-zinc-50 text-zinc-900 dark:border-zinc-800 dark:bg-zinc-900 hover:dark:bg-zinc-800 dark:text-white',
			outerButtonIconClass: 'h-3 w-3',
			numberButtonClass: 'block h-8 w-8 rounded border text-center leading-8'
		},
		variants: {
			active: {
				true: {
					numberButtonClass:
						'border-blue-600 bg-blue-600 text-white dark:text-white hover:bg-blue-500'
				},
				false: {
					numberButtonClass:
						'border-zinc-100 bg-white text-zinc-900 dark:border-zinc-800 dark:bg-zinc-900 dark:text-white hover:bg-zinc-50 hover:dark:bg-zinc-800'
				}
			}
		}
	});
</script>

<script lang="ts">
	import { ChevronLeftIcon, ChevronRightIcon, Icon } from '../icons';

	let className: string = '';
	export { className as class };

	export let page: number;
	export let totalPages: number = 1;
	export let clickableNumbersAroundPage: number = 3;

	// Get start and end values of clickable numbers
	$: clickableFirstNumber = Math.max(page - clickableNumbersAroundPage, 1);
	$: clickableLastNumber = Math.min(page + clickableNumbersAroundPage, totalPages);

	// Create array of values between clickableFirstNumber and clickableLastNumber
	function toRangeArray(start: number, end: number): number[] {
		return Array.from({ length: end - start + 1 }, (_v, index) => index + start);
	}
	$: clickableNumbers = toRangeArray(clickableFirstNumber, clickableLastNumber);

	const { containerClass, outerButtonClass, outerButtonIconClass, numberButtonClass } =
		paginationClasses();
</script>

<ol {...$$restProps} class={containerClass({ class: className })}>
	<li>
		<button on:click={() => (page = Math.max(page - 1, 1))} class={outerButtonClass()}>
			<span class="sr-only">Prev Page</span>
			<Icon src={ChevronLeftIcon} theme="solid" class={outerButtonIconClass()} />
		</button>
	</li>
	{#each clickableNumbers as n}
		<li>
			<button on:click={() => (page = n)} class={numberButtonClass({ active: page == n })}>
				{n}
			</button>
		</li>
	{/each}
	<li>
		<button on:click={() => (page = Math.min(page + 1, totalPages))} class={outerButtonClass()}>
			<span class="sr-only">Next Page</span>
			<Icon src={ChevronRightIcon} theme="solid" class={outerButtonIconClass()} />
		</button>
	</li>
</ol>
