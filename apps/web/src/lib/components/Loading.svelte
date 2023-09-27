<script lang="ts">
	import { Icon, LoaderIcon } from '@yd/ui';
</script>

<div
	class="-mt-16 flex h-screen flex-col items-center justify-center space-y-2 text-zinc-900 dark:text-white"
>
	<Icon src={LoaderIcon} class="h-10 w-10 animate-spin" />
	<div>Setting up session...</div>
</div>
