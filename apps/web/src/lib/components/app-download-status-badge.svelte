<script lang="ts">
	import { toClassFromState, toIconFromState, toTextFromStatus } from '$lib/utils/status';

	import type { DownloadStatus } from '@yd/client';
	import { Badge } from '@yd/ui';

	interface Props {
		status: DownloadStatus;
	}

	let { status }: Props = $props();

	let text = $derived(toTextFromStatus(status));
	let IconComponent = $derived(toIconFromState(status.state));
</script>

<div>
	<Badge variant="secondary" class={toClassFromState(status.state)}>
		<IconComponent class="mr-1 size-5" />
		{text}
		{status.progress ? `${Math.trunc(status.progress)}%` : ''}
	</Badge>
</div>
