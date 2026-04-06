<script lang="ts">
	import type { RouteItem } from '$lib/routes';
	import type { ComponentProps } from 'svelte';
	import { resolve } from '$app/paths';
	import { page } from '$app/state';
	import { routes } from '$lib/routes';

	import { ChevronRightIcon, Collapsible, Sidebar } from '@yd/ui';

	let { ref = $bindable(null), ...restProps }: ComponentProps<typeof Sidebar.Root> = $props();
</script>

{#snippet sidebaritem(item: RouteItem)}
	<Collapsible.Root open={true}>
		{#snippet child({ props })}
			<Sidebar.MenuItem {...props}>
				<Sidebar.MenuButton tooltipContent={item.title} isActive={page.route.id === item.url}>
					Test
					{#snippet child({ props })}
						<!-- eslint-disable svelte/no-navigation-without-resolve -->
						<a
							href={item.url}
							target={item.external ? '_blank' : undefined}
							rel={item.external ? 'noreferrer' : undefined}
							{...props}
						>
							<item.icon />
							<span>{item.title}</span>
						</a>
						<!-- eslint-enable svelte/no-navigation-without-resolve -->
					{/snippet}
				</Sidebar.MenuButton>
				{#if item.items?.length}
					<Collapsible.Trigger>
						{#snippet child({ props })}
							<Sidebar.MenuAction {...props} class="data-[state=open]:rotate-90">
								<ChevronRightIcon />
								<span class="sr-only">Toggle</span>
							</Sidebar.MenuAction>
						{/snippet}
					</Collapsible.Trigger>
					<Collapsible.Content>
						<Sidebar.MenuSub>
							{#each item.items as subItem (subItem.title)}
								<Sidebar.MenuSubItem>
									<Sidebar.MenuSubButton
										href={subItem.url}
										isActive={page.route.id === subItem.url}
									>
										<span>{subItem.title}</span>
									</Sidebar.MenuSubButton>
								</Sidebar.MenuSubItem>
							{/each}
						</Sidebar.MenuSub>
					</Collapsible.Content>
				{/if}
			</Sidebar.MenuItem>
		{/snippet}
	</Collapsible.Root>
{/snippet}

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
					{@render sidebaritem(item)}
				{/each}
			</Sidebar.Menu>
		</Sidebar.Group>
	</Sidebar.Content>
	<Sidebar.Footer>
		<Sidebar.Menu class="my-2">
			{#each routes.footer as item (item.title)}
				{@render sidebaritem(item)}
			{/each}
		</Sidebar.Menu>
	</Sidebar.Footer>
</Sidebar.Root>
