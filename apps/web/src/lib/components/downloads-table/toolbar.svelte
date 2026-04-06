<script lang="ts">
	import type { Download } from '@yd/client';
	import type { TableType } from '@yd/ui';
	import { Button, Input, XIcon } from '@yd/ui';

	import ViewOptions from './view-options.svelte';

	let { table }: { table: TableType<Download> } = $props();

	const isFiltered = $derived(table.getState().columnFilters.length > 0);
	const column = $derived(table.getColumn('video'));
</script>

<div class="flex items-center justify-between">
	<div class="flex flex-1 items-center space-x-2">
		<Input.Root
			placeholder="Filter downloads..."
			value={(column?.getFilterValue() as string) ?? ''}
			oninput={(e) => {
				column?.setFilterValue(e.currentTarget.value);
			}}
			onchange={(e) => {
				column?.setFilterValue(e.currentTarget.value);
			}}
			class="h-8 w-37.5 lg:w-62.5"
		/>
		{#if isFiltered}
			<Button.Root
				variant="ghost"
				onclick={() => table.resetColumnFilters()}
				class="h-8 px-2 lg:px-3"
			>
				Reset
				<XIcon />
			</Button.Root>
		{/if}
	</div>
	<ViewOptions {table} />
</div>
