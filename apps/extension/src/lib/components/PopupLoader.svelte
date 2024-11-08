<script lang="ts">
	import { Icon, LoaderIcon } from '@yd/ui';

	interface Props {
		message?: string;
	}

	let { message = 'Loading...' }: Props = $props();
</script>

<div class="flex h-full flex-col items-center justify-center space-y-2">
	<Icon src={LoaderIcon} class="h-10 w-10 animate-spin" />
	<div>{message}</div>
</div>
