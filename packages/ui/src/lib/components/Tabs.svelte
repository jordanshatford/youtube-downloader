<script lang="ts">
	import { tv } from 'tailwind-variants';
	import { Icon, type IconSource } from '../icons';

	const tabsClasses = tv({
		slots: {
			selectClass:
				'w-full rounded-lg border-2 border-zinc-200 p-2 text-zinc-600 outline-none focus:ring-transparent focus:border-blue-600 dark:focus:border-blue-600 dark:border-zinc-600 dark:bg-zinc-800 dark:text-zinc-200 dark:disabled:bg-zinc-600',
			tabsWrapperDivClass: 'border-b border-gray-200 dark:border-gray-700',
			tabsNavClass: '-mb-px flex gap-2',
			buttonClass:
				'inline-flex shrink-0 items-center gap-1 border-b-2 px-2 py-3 text-sm font-medium',
			iconClass: 'h-5 w-5'
		},
		variants: {
			active: {
				true: {
					buttonClass: 'border-blue-600 text-blue-600 dark:border-blue-500 dark:text-blue-500'
				},
				false: {
					buttonClass:
						'border-transparent text-gray-500 hover:border-gray-300 hover:text-gray-700 dark:text-gray-400 dark:hover:border-gray-600 dark:hover:text-gray-200'
				}
			}
		}
	});

	export let active: string;
	export let tabs: { key: string; title: string; icon?: IconSource }[] = [];

	const { selectClass, tabsWrapperDivClass, tabsNavClass, buttonClass, iconClass } = tabsClasses();
</script>

<div {...$$restProps}>
	<!-- On small devices show a select -->
	<div class="sm:hidden">
		<label for="Tab" class="sr-only">Tab</label>
		<select id="Tab" class={selectClass()} bind:value={active}>
			{#each tabs as tab}
				<option value={tab.key}>{tab.title}</option>
			{/each}
		</select>
	</div>
	<!-- On larger devices show the bigger tabs with icons -->
	<div class="hidden sm:block">
		<div class={tabsWrapperDivClass()}>
			<nav class={tabsNavClass()} aria-label="Tabs">
				{#each tabs as tab (tab.key)}
					<button
						on:click={() => (active = tab.key)}
						class={buttonClass({ active: tab.key === active })}
					>
						{#if tab.icon}
							<Icon src={tab.icon} class={iconClass()} />
						{/if}
						{tab.title}
					</button>
				{/each}
			</nav>
		</div>
	</div>
</div>
