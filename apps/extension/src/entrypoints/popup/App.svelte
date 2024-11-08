<script lang="ts">
	import PopupLayout from '~/lib/components/PopupLayout.svelte';
	import PopupMain from '~/lib/components/PopupMain.svelte';
</script>

<PopupLayout>
	{#snippet children({ ctx })}
		<PopupMain {ctx} />
	{/snippet}
</PopupLayout>
