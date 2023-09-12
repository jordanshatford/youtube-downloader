import type { Variant } from './types';
import {
	type IconSource,
	ExclamationCircleIcon,
	ExclamationTriangleIcon,
	CheckCircleIcon,
	InformationCircleIcon,
	MinusCircleIcon
} from './icons';

export const variantMapping: Record<Variant, { icon: IconSource; class: string }> = {
	error: {
		icon: ExclamationCircleIcon,
		class: 'text-red-800 bg-red-200'
	},
	warning: {
		icon: ExclamationTriangleIcon,
		class: 'text-yellow-600 bg-yellow-200'
	},
	info: {
		icon: InformationCircleIcon,
		class: 'text-blue-800 bg-blue-200'
	},
	success: {
		icon: CheckCircleIcon,
		class: 'text-green-700 bg-green-200'
	},
	default: {
		icon: MinusCircleIcon,
		class: 'bg-zinc-400 text-zinc-800'
	}
};
