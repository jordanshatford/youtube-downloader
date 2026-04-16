import '../app.css';

// shadcn component exports (see: https://shadcn-svelte.com/)
export * as Accordion from '$uilib/components/ui/accordion/index';
export * as Alert from '$uilib/components/ui/alert/index';
export * as AlertDialog from '$uilib/components/ui/alert-dialog/index';
export { Badge, type BadgeVariant, badgeVariants } from '$uilib/components/ui/badge/index';
export * as Breadcrumb from '$uilib/components/ui/breadcrumb/index';
export * as Button from '$uilib/components/ui/button/index';
export { buttonVariants } from '$uilib/components/ui/button/index';
export * as Checkbox from '$uilib/components/ui/checkbox/index';
export * as Collapsible from '$uilib/components/ui/collapsible/index';
export * as DropdownMenu from '$uilib/components/ui/dropdown-menu/index';
export * as Empty from '$uilib/components/ui/empty/index';
export * as Field from '$uilib/components/ui/field/index';
export * as Input from '$uilib/components/ui/input/index';
export * as InputGroup from '$uilib/components/ui/input-group/index';
export * as Item from '$uilib/components/ui/item/index';
export * as Select from '$uilib/components/ui/select/index';
export * as Separator from '$uilib/components/ui/separator/index';
export { useSidebar } from '$uilib/components/ui/sidebar/context.svelte';
export * as Sidebar from '$uilib/components/ui/sidebar/index';
export * as Table from '$uilib/components/ui/table/index';
export * as Tabs from '$uilib/components/ui/tabs/index';
export * as Tooltip from '$uilib/components/ui/tooltip/index';
export {
	FlexRender,
	createSvelteTable,
	renderComponent
} from '$uilib/components/ui/data-table/index';
export { cn } from '$uilib/utils';

// lucide icons exports (see: https://lucide.dev/)
export { default as AlertCircleIcon } from '@lucide/svelte/icons/alert-circle';
export { default as ArrowUpRightIcon } from '@lucide/svelte/icons/arrow-up-right';
export { default as BanIcon } from '@lucide/svelte/icons/ban';
export { default as BracesIcon } from '@lucide/svelte/icons/braces';
export { default as BugIcon } from '@lucide/svelte/icons/bug';
export { default as CheckCircleIcon } from '@lucide/svelte/icons/circle-check';
export { default as ChevronRightIcon } from '@lucide/svelte/icons/chevron-right';
export { default as CircleQuestionMarkIcon } from '@lucide/svelte/icons/circle-question-mark';
export { default as CodeIcon } from '@lucide/svelte/icons/code';
export { default as CopyrightIcon } from '@lucide/svelte/icons/copyright';
export { default as DownloadIcon } from '@lucide/svelte/icons/download';
export { default as FileDownloadIcon } from '@lucide/svelte/icons/file-down';
export { default as EllipsisIcon } from '@lucide/svelte/icons/ellipsis';
export { default as GitPullRequestIcon } from '@lucide/svelte/icons/git-pull-request';
export { default as HandshakeIcon } from '@lucide/svelte/icons/handshake';
export { default as MoonIcon } from '@lucide/svelte/icons/moon';
export { default as PlusIcon } from '@lucide/svelte/icons/plus';
export { default as RotateIcon } from '@lucide/svelte/icons/rotate-ccw';
export { default as SearchIcon } from '@lucide/svelte/icons/search';
export { default as SettingsIcon } from '@lucide/svelte/icons/settings';
export { default as Settings2Icon } from '@lucide/svelte/icons/settings-2';
export { Spinner as SpinnerIcon } from '$uilib/components/ui/spinner/index';
export { default as SunIcon } from '@lucide/svelte/icons/sun';
export { default as TrashIcon } from '@lucide/svelte/icons/trash-2';
export { default as ArrowUpIcon } from '@lucide/svelte/icons/arrow-up';
export { default as ArrowDownIcon } from '@lucide/svelte/icons/arrow-down';
export { default as ChevronsUpDownIcon } from '@lucide/svelte/icons/chevrons-up-down';
export { default as EyeOffIcon } from '@lucide/svelte/icons/eye-off';
export { default as ChevronLeftIcon } from '@lucide/svelte/icons/chevron-left';
export { default as ChevronsLeftIcon } from '@lucide/svelte/icons/chevrons-left';
export { default as ChevronsRightIcon } from '@lucide/svelte/icons/chevrons-right';
export { default as XIcon } from '@lucide/svelte/icons/x';
export { default as ScrollIcon } from '@lucide/svelte/icons/scroll-text';
export { default as MonitorPlayIcon } from '@lucide/svelte/icons/monitor-play';
export { default as CornerDownLeftIcon } from '@lucide/svelte/icons/corner-down-left';
export { default as GalleryVerticalEndIcon } from '@lucide/svelte/icons/gallery-vertical-end';

// mode-watcher related exports (see: https://github.com/svecosystem/mode-watcher#readme)
export { ModeWatcher, toggleMode } from 'mode-watcher';

// svelte-sonner related exports (see: https://svelte-sonner.vercel.app/)
export { Toaster } from '$uilib/components/ui/sonner/index';
export { toast } from 'svelte-sonner';

// tanstack/table-core related exports (see: https://tanstack.com/table/latest)
export type {
	Column,
	ColumnDef,
	ColumnFiltersState,
	OnChangeFn,
	PaginationState,
	Row,
	RowSelectionState,
	SortingState,
	VisibilityState,
	Table as TableType
} from '@tanstack/table-core';
export {
	getCoreRowModel,
	getFacetedRowModel,
	getFacetedUniqueValues,
	getFilteredRowModel,
	getPaginationRowModel,
	getSortedRowModel
} from '@tanstack/table-core';
