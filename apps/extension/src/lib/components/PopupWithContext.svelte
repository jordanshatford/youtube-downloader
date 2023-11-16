<script lang="ts">
	import { getContextService } from '~/lib/context-service';
	import PopupLayout from '~/lib/components/PopupLayout.svelte';
	import PopupLoader from '~/lib/components/PopupLoader.svelte';
	import PopupError from '~/lib/components/PopupError.svelte';

	// Get context service.
	const context = getContextService();
</script>

<PopupLayout>
	{#await context.get()}
		<!-- Loader shown while awaiting context -->
		<PopupLoader />
	{:then ctx}
		<!-- Slot show when context found -->
		<slot {ctx} />
	{:catch}
		<!-- Could not get context -->
		<PopupError message="Could not detect YouTube video in active tab." />
	{/await}
</PopupLayout>
