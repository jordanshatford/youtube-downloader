<script lang="ts">
	import type { Snippet } from 'svelte';
	import { page } from '$app/state';
	import { settingsRoutes } from '$lib/routes';

	import { Tabs } from '@yd/ui';

	interface Props {
		children?: Snippet;
	}

	let { children }: Props = $props();
</script>

<Tabs.Root value={page.url.pathname} class="mx-auto max-w-2xl">
	<Tabs.List>
		<!-- eslint-disable svelte/no-navigation-without-resolve -->
		{#each settingsRoutes as route (route.url)}
			<Tabs.Trigger value={route.url}>
				{#snippet child({ props })}
					<a href={route.url} {...props}><route.icon /> {route.title}</a>
				{/snippet}
			</Tabs.Trigger>
		{/each}
		<!-- eslint-enable svelte/no-navigation-without-resolve -->
	</Tabs.List>
	{@render children?.()}
</Tabs.Root>
