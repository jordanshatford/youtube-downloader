<script lang="ts">
	import { Variant } from '$lib/utils/types';

	export let variant: Variant = Variant.DEFAULT;

	let className: string;

	$: switch (variant) {
		case Variant.WARNING:
			className = 'bg-yellow-200 text-yellow-800';
			break;
		case Variant.INFO:
			className = 'bg-blue-200 text-blue-800';
			break;
		case Variant.SUCCESS:
			className = 'bg-green-200 text-green-800';
			break;
		case Variant.DANGER:
			className = 'bg-red-200 text-red-800';
			break;
		default:
			className = 'bg-zinc-400 text-zinc-800';
			break;
	}
</script>

<div class="rounded-lg flex items-center justify-center {className}">
	<div class="rounded-lg flex items-center justify-center h-full w-full">
		<slot />
	</div>
</div>
