<script lang="ts">
	import type { Download } from '@yd/client';
	import type {
		ColumnDef,
		ColumnFiltersState,
		PaginationState,
		RowSelectionState,
		SortingState,
		VisibilityState
	} from '@yd/ui';
	import {
		// Checkbox,
		createSvelteTable,
		FlexRender,
		getCoreRowModel,
		getFacetedRowModel,
		getFacetedUniqueValues,
		getFilteredRowModel,
		getPaginationRowModel,
		getSortedRowModel,
		renderComponent,
		Table
	} from '@yd/ui';

	import AppDownloadStatusBadge from '../app-download-status-badge.svelte';
	import AppVideoInfo from '../app-video-info.svelte';
	import ActionsCell from './actions-cell.svelte';
	import BadgesCell from './badges-cell.svelte';
	import ColumnHeader from './column-header.svelte';
	import Pagination from './pagination.svelte';
	import Toolbar from './toolbar.svelte';

	let { data }: { data: Download[] } = $props();

	let rowSelection = $state<RowSelectionState>({});
	let columnVisibility = $state<VisibilityState>({
		embed: false,
		quality: false
	});
	let columnFilters = $state<ColumnFiltersState>([]);
	let sorting = $state<SortingState>([]);
	let pagination = $state<PaginationState>({ pageIndex: 0, pageSize: 10 });

	const columns: ColumnDef<Download>[] = [
		// {
		// 	id: 'select',
		// 	header: ({ table }) =>
		// 		renderComponent(Checkbox.Root, {
		// 			checked: table.getIsAllPageRowsSelected(),
		// 			onCheckedChange: (value) => table.toggleAllPageRowsSelected(value),
		// 			indeterminate: table.getIsSomePageRowsSelected() && !table.getIsAllPageRowsSelected(),
		// 			'aria-label': 'Select all'
		// 		}),
		// 	cell: ({ row }) =>
		// 		renderComponent(Checkbox.Root, {
		// 			checked: row.getIsSelected(),
		// 			onCheckedChange: (value) => row.toggleSelected(value),
		// 			'aria-label': 'Select row'
		// 		}),
		// 	enableSorting: false,
		// 	enableHiding: false
		// },
		{
			id: 'video',
			accessorFn: (row) => row.video.title,
			header: ({ column }) => {
				return renderComponent(ColumnHeader, {
					column,
					title: 'Video'
				});
			},
			cell: ({ row }) => {
				return renderComponent(AppVideoInfo, {
					video: row.original.video,
					size: 'sm'
				});
			},
			enableHiding: false
		},
		{
			id: 'format',
			accessorFn: (row) => row.options.format,
			header: ({ column }) =>
				renderComponent(ColumnHeader, {
					column,
					title: 'Format'
				}),
			cell: ({ row }) => {
				return renderComponent(BadgesCell, {
					items: [row.original.options.format?.toUpperCase() ?? '']
				});
			},
			filterFn: (row, id, value) => {
				return value.includes(row.getValue(id));
			}
		},
		{
			id: 'quality',
			accessorFn: (row) => row.options.quality,
			header: ({ column }) =>
				renderComponent(ColumnHeader, {
					column,
					title: 'Quality'
				}),
			cell: ({ row }) => {
				const quality = row.original.options.quality;
				let item = '';
				if (quality) {
					item = quality?.charAt(0).toUpperCase() + quality?.slice(1);
				}
				return renderComponent(BadgesCell, {
					items: [item]
				});
			},
			enableSorting: false
		},
		{
			accessorKey: 'embed',
			header: ({ column }) =>
				renderComponent(ColumnHeader, {
					column,
					title: 'Embed'
				}),
			cell: ({ row }) => {
				const items: string[] = [];
				const options = row.original.options;
				if (options.embed_metadata) {
					items.push('Metadata');
				}
				if (options.embed_thumbnail) {
					items.push('Thumbnail');
				}
				if (options.embed_subtitles) {
					items.push('Subtitles');
				}
				if (!options.embed_metadata && !options.embed_thumbnail && !options.embed_subtitles) {
					items.push('None');
				}
				return renderComponent(BadgesCell, {
					items
				});
			},
			enableSorting: false
		},
		{
			id: 'status',
			accessorFn: (row) => row.status.state,
			header: ({ column }) => {
				return renderComponent(ColumnHeader, {
					title: 'Status',
					column
				});
			},
			cell: ({ row }) => {
				return renderComponent(AppDownloadStatusBadge, {
					status: row.original.status
				});
			},
			filterFn: (row, id, value) => {
				return value.includes(row.getValue(id));
			}
		},
		{
			id: 'actions',
			// header: ({ table }) => {
			// 	const rows = table.getSelectedRowModel().rows
			// 	return renderComponent(ActionsCell, { rows, disabled: rows.length === 0 });
			// },
			cell: ({ row }) => {
				return renderComponent(ActionsCell, { row });
			},
			enableSorting: false,
			enableHiding: false
		}
	];

	const table = createSvelteTable({
		get data() {
			return data;
		},
		state: {
			get sorting() {
				return sorting;
			},
			get columnVisibility() {
				return columnVisibility;
			},
			get rowSelection() {
				return rowSelection;
			},
			get columnFilters() {
				return columnFilters;
			},
			get pagination() {
				return pagination;
			}
		},
		columns,
		enableRowSelection: true,
		onRowSelectionChange: (updater) => {
			if (typeof updater === 'function') {
				rowSelection = updater(rowSelection);
			} else {
				rowSelection = updater;
			}
		},
		onSortingChange: (updater) => {
			if (typeof updater === 'function') {
				sorting = updater(sorting);
			} else {
				sorting = updater;
			}
		},
		onColumnFiltersChange: (updater) => {
			if (typeof updater === 'function') {
				columnFilters = updater(columnFilters);
			} else {
				columnFilters = updater;
			}
		},
		onColumnVisibilityChange: (updater) => {
			if (typeof updater === 'function') {
				columnVisibility = updater(columnVisibility);
			} else {
				columnVisibility = updater;
			}
		},
		onPaginationChange: (updater) => {
			if (typeof updater === 'function') {
				pagination = updater(pagination);
			} else {
				pagination = updater;
			}
		},
		getCoreRowModel: getCoreRowModel(),
		getFilteredRowModel: getFilteredRowModel(),
		getPaginationRowModel: getPaginationRowModel(),
		getSortedRowModel: getSortedRowModel(),
		getFacetedRowModel: getFacetedRowModel(),
		getFacetedUniqueValues: getFacetedUniqueValues()
	});
</script>

<div class="space-y-4">
	<Toolbar {table} />
	<div class="rounded-md border">
		<Table.Root>
			<Table.Header>
				{#each table.getHeaderGroups() as headerGroup (headerGroup.id)}
					<Table.Row>
						{#each headerGroup.headers as header (header.id)}
							<Table.Head colspan={header.colSpan}>
								{#if !header.isPlaceholder}
									<FlexRender
										content={header.column.columnDef.header}
										context={header.getContext()}
									/>
								{/if}
							</Table.Head>
						{/each}
					</Table.Row>
				{/each}
			</Table.Header>
			<Table.Body>
				{#each table.getRowModel().rows as row (row.id)}
					<Table.Row data-state={row.getIsSelected() && 'selected'}>
						{#each row.getVisibleCells() as cell (cell.id)}
							<Table.Cell>
								<FlexRender content={cell.column.columnDef.cell} context={cell.getContext()} />
							</Table.Cell>
						{/each}
					</Table.Row>
				{:else}
					<Table.Row>
						<Table.Cell colspan={columns.length} class="h-24 text-center">No downloads.</Table.Cell>
					</Table.Row>
				{/each}
			</Table.Body>
		</Table.Root>
	</div>
	<Pagination {table} />
</div>
