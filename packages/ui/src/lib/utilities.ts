import type { Variant } from './types';
import {
	AlertCircleIcon,
	AlertTriangleIcon,
	CheckCircleIcon,
	InfoIcon,
	MinusCircleIcon
} from './icons';

export const variantMapping: Record<Variant, { icon: typeof MinusCircleIcon; class: string }> = {
	error: {
		icon: AlertCircleIcon,
		class: 'text-red-800 bg-red-200'
	},
	warning: {
		icon: AlertTriangleIcon,
		class: 'text-yellow-600 bg-yellow-200'
	},
	info: {
		icon: InfoIcon,
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
