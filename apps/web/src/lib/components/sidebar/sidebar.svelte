<script lang="ts">
	import type { ComponentProps } from 'svelte';
	import { resolve } from '$app/paths';
	import { routes } from '$lib/routes';

	import { Sidebar } from '@yd/ui';

	import SidebarItem from './sidebar-item.svelte';

	let { ref = $bindable(null), ...restProps }: ComponentProps<typeof Sidebar.Root> = $props();
</script>

<Sidebar.Root bind:ref {...restProps}>
	<Sidebar.Header>
		<Sidebar.Menu>
			<Sidebar.MenuItem>
				<Sidebar.MenuButton size="lg" tooltipContent="YouTube Downloader">
					{#snippet child({ props })}
						<a href={resolve('/')} {...props}>
							<div
								class="bg-sidebar-primary text-sidebar-primary-foreground flex aspect-square size-8 items-center justify-center rounded-md"
							>
								<img class="size=8 block w-auto" src="icon.png" alt="Logo" />
							</div>
							<div class="grid flex-1 text-start text-sm leading-tight">
								<span class="truncate font-medium">YouTube Downloader</span>
							</div>
						</a>
					{/snippet}
				</Sidebar.MenuButton>
			</Sidebar.MenuItem>
		</Sidebar.Menu>
	</Sidebar.Header>
	<Sidebar.Content>
		<Sidebar.Group>
			<Sidebar.Menu>
				{#each routes.main as item (item.title)}
					<SidebarItem {item} />
				{/each}
			</Sidebar.Menu>
		</Sidebar.Group>
	</Sidebar.Content>
	<Sidebar.Footer>
		<Sidebar.Menu class="my-2">
			{#each routes.footer as item (item.title)}
				<SidebarItem {item} />
			{/each}
		</Sidebar.Menu>
	</Sidebar.Footer>
</Sidebar.Root>
