// Base icon component and typings
export { Icon, type IconSource } from '@steeze-ui/svelte-icon';

// Icon sources reexported for use
export {
	CheckCircle as CheckCircleIcon,
	ChevronLeft as ChevronLeftIcon,
	ChevronRight as ChevronRightIcon,
	ArrowDownTray as DownloadIcon,
	ExclamationCircle as ExclamationCircleIcon,
	ExclamationTriangle as ExclamationTriangleIcon,
	Cog6Tooth as GearIcon,
	InformationCircle as InformationCircleIcon,
	MagnifyingGlass as MagnifyingGlassIcon,
	Bars3 as MenuIcon,
	MinusCircle as MinusCircleIcon,
	Moon as MoonIcon,
	Plus as PlusIcon,
	PlusCircle as PlusCircleIcon,
	ArrowPath as ArrowPathIcon,
	Sun as SunIcon,
	Trash as TrashIcon,
	XMark as XMarkIcon
} from '@steeze-ui/heroicons';

export { Github as GithubIcon } from '@steeze-ui/simple-icons';

// Custom icons exported for use
import type { IconSource } from '@steeze-ui/svelte-icon';

const LoaderIcon: IconSource = {
	default: {
		a: {
			fill: 'none',
			viewBox: '0 0 24 24',
			'stroke-width': '2',
			stroke: 'currentColor',
			'aria-hidden': 'true'
		},
		path: [
			{
				class: 'stroke-current opacity-25',
				'stroke-linecap': 'round',
				'stroke-linejoin': 'round',
				d: 'M12 22C17.5228 22 22 17.5228 22 12C22 6.47715 17.5228 2 12 2C6.47715 2 2 6.47715 2 12C2 17.5228 6.47715 22 12 22Z',
				'clip-rule': 'evenodd'
			},
			{
				'stroke-linecap': 'round',
				'stroke-linejoin': 'round',
				d: 'M12 2C6.47715 2 2 6.47715 2 12C2 14.7255 3.09032 17.1962 4.85857 19',
				'clip-rule': 'evenodd'
			}
		]
	}
};

export { LoaderIcon };
