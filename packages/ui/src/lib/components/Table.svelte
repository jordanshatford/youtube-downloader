<script lang="ts" generics="T extends object">
	import type { Snippet } from 'svelte';

	const classes = {
		table: 'min-w-full divide-y divide-zinc-200 dark:divide-zinc-800 table-auto',
		headtr: '',
		thead: 'bg-zinc-50 dark:bg-zinc-800',
		tbody: 'bg-white dark:bg-zinc-900 divide-y divide-zinc-200 dark:divide-zinc-800',
		tr: '',
		th: 'px-6 py-3 text-left text-xs font-medium text-zinc-500 dark:text-white uppercase',
		td: 'px-6 py-4 whitespace-nowrap text-zinc-500 dark:text-zinc-300'
	};

	type TCol = { key: string; title: string };
	type TRow = T;
	interface Props {
		columns?: TCol[];
		rows?: TRow[];
		head?: Snippet<[{ column: TCol }]>;
		cell?: Snippet<[{ column: TCol; row: TRow }]>;
		empty?: Snippet;
	}

	let { columns = [], rows = [], head, cell, empty }: Props = $props();

	function isLastColumn(index: number) {
		return index === columns.length - 1;
	}
</script>

<table class={classes.table} cellspacing="0">
	<thead class={classes.thead}>
		<tr class={classes.headtr}>
			{#each columns as column, index}
				{@const isLastCol = isLastColumn(index) ? 'text-right' : ''}
				<th scope="col" class={`${classes.th} ${isLastCol}`}>
					{#if head}
						{@render head?.({ column })}
					{:else}
						<span>{column.title}</span>
					{/if}
				</th>
			{/each}
		</tr>
	</thead>
	<tbody class={classes.tbody}>
		{#each rows as row}
			<tr class={classes.tr}>
				{#each columns as column, index}
					{@const isLastCol = isLastColumn(index) ? 'text-right' : ''}
					<td class={`${classes.td} ${isLastCol}`}>
						{#if cell}
							{@render cell?.({ row, column })}
						{:else}
							<span></span>
						{/if}
					</td>
				{/each}
			</tr>
		{:else}
			{@render empty?.()}
		{/each}
	</tbody>
</table>
