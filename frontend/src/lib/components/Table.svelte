<script lang="ts" context="module">
	export interface TableColumn {
		key: string;
		title: string;
	}
</script>

<script lang="ts">
	type T = $$Generic<Record<string, unknown>>;
	export let columns: TableColumn[] = [];
	export let rows: T[] = [];

	const defaultClasses = {
		table: 'min-w-full divide-y divide-zinc-200 dark:divide-zinc-800 table-auto',
		headtr: '',
		thead: 'bg-zinc-50 dark:bg-zinc-800',
		tbody: 'bg-white dark:bg-zinc-900 divide-y divide-zinc-200 dark:divide-zinc-800',
		tr: '',
		th: 'px-6 py-3 text-left text-xs font-medium text-zinc-500 dark:text-white uppercase',
		td: 'px-6 py-4 whitespace-nowrap text-zinc-500 dark:text-zinc-300'
	};
	export let classes = defaultClasses;

	$: assignedClasses = { ...defaultClasses, ...classes };

	function isLastColumn(index: number) {
		return index === columns.length - 1;
	}
</script>

<table class={assignedClasses.table} cellspacing="0">
	<thead class={assignedClasses.thead}>
		<tr class={assignedClasses.headtr}>
			{#each columns as column, index}
				{@const isLastCol = isLastColumn(index) ? 'text-right' : ''}
				<th scope="col" class={`${assignedClasses.th} ${isLastCol}`}>
					{#if $$slots.head}
						<slot name="head" {column} />
					{:else}
						<span>{column.title}</span>
					{/if}
				</th>
			{/each}
		</tr>
	</thead>
	<tbody class={assignedClasses.tbody}>
		{#each rows as row}
			<tr class={assignedClasses.tr}>
				{#each columns as column, index}
					{@const isLastCol = isLastColumn(index) ? 'text-right' : ''}
					<td class={`${assignedClasses.td} ${isLastCol}`}>
						{#if $$slots.cell}
							<slot name="cell" {row} {column} cell={row[column.key]} />
						{:else}
							<span>{row[column.key]}</span>
						{/if}
					</td>
				{/each}
			</tr>
		{:else}
			<slot name="empty" />
		{/each}
	</tbody>
</table>
