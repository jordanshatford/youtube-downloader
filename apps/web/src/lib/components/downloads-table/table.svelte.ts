import type {
	ColumnFiltersState,
	OnChangeFn,
	PaginationState,
	RowSelectionState,
	SortingState,
	VisibilityState
} from '@yd/ui';

class TableStore {
	public sorting = $state<SortingState>([]);
	public selection = $state<RowSelectionState>({});
	public pagination = $state<PaginationState>({ pageIndex: 0, pageSize: 10 });
	public columnVisibility = $state<VisibilityState>({
		duration: false,
		embed: false,
		quality: false
	});
	public columnFilters = $state<ColumnFiltersState>([]);

	public onSortingChange: OnChangeFn<SortingState> = (updater) => {
		if (typeof updater === 'function') {
			this.sorting = updater(this.sorting);
		} else {
			this.sorting = updater;
		}
	};

	public onRowSelectionChange: OnChangeFn<RowSelectionState> = (updater) => {
		if (typeof updater === 'function') {
			this.selection = updater(this.selection);
		} else {
			this.selection = updater;
		}
	};

	public onPaginationChange: OnChangeFn<PaginationState> = (updater) => {
		if (typeof updater === 'function') {
			this.pagination = updater(this.pagination);
		} else {
			this.pagination = updater;
		}
	};

	public onColumnVisibilityChange: OnChangeFn<VisibilityState> = (updater) => {
		if (typeof updater === 'function') {
			this.columnVisibility = updater(this.columnVisibility);
		} else {
			this.columnVisibility = updater;
		}
	};

	public onColumnFiltersChange: OnChangeFn<ColumnFiltersState> = (updater) => {
		if (typeof updater === 'function') {
			this.columnFilters = updater(this.columnFilters);
		} else {
			this.columnFilters = updater;
		}
	};
}

export const tableStore = new TableStore();
