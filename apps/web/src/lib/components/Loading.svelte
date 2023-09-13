<script lang="ts">
	import { Icon, LoaderIcon } from '@yd/ui';
</script>

<div class="bg-white dark:bg-zinc-900">
	<div class="flex h-screen">
		<div class="m-auto text-center">
			<div class="w-100 relative inline-block overflow-hidden align-middle">
				<div class="h-48 text-zinc-900 dark:text-white">
					<Icon src={LoaderIcon} class="h-50 relative inline-block animate-spin" />
					<img class="absolute inset-6 h-36 w-auto" src="images/logo.png" alt="Logo" />
				</div>
			</div>
		</div>
	</div>
</div>
