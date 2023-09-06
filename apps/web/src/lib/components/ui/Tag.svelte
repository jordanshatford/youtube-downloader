<script lang="ts">
	import type { Variant } from '@yd/ui';

	export let variant: Variant = 'default';

	let className: string;

	$: switch (variant) {
		case 'warning':
			className = 'bg-yellow-200 text-yellow-800';
			break;
		case 'info':
			className = 'bg-blue-200 text-blue-800';
			break;
		case 'success':
			className = 'bg-green-200 text-green-800';
			break;
		case 'error':
			className = 'bg-red-200 text-red-800';
			break;
		case 'default':
			className = 'bg-zinc-400 text-zinc-800';
			break;
	}
</script>

<div class="rounded-lg flex items-center justify-center {className}">
	<div class="rounded-lg flex items-center justify-center h-full w-full">
		<slot />
	</div>
</div>
