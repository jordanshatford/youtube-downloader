<script lang="ts">
	import { toClassFromStateNew, toIconFromState, toTextFromStatus } from '$lib/utils/status';

	import type { DownloadStatus } from '@yd/client';
	import { buttonVariants, Tooltip } from '@yd/ui';

	interface Props {
		status: DownloadStatus;
	}

	let { status }: Props = $props();

	let text = $derived(toTextFromStatus(status));
	let IconComponent = $derived(toIconFromState(status.state));
</script>

<Tooltip.Provider>
	<Tooltip.Root>
		<Tooltip.Trigger aria-disabled class={buttonVariants({ variant: 'outline', size: 'icon' })}>
			<IconComponent class={toClassFromStateNew(status.state)} />
		</Tooltip.Trigger>
		<Tooltip.Content>
			{text}
		</Tooltip.Content>
	</Tooltip.Root>
</Tooltip.Provider>
