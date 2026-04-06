<script lang="ts">
	import type { RouteItem } from '$lib/routes';
	import { page } from '$app/state';
	import { downloads } from '$lib/stores/downloads.svelte';

	import { Badge, badgeVariants, ChevronRightIcon, Collapsible, Sidebar, useSidebar } from '@yd/ui';

	let { item }: { item: RouteItem } = $props();

	let sidebar = useSidebar();

	let count = $derived.by(() => {
		if (item.url !== '/downloads') {
			return undefined;
		}
		const len = Object.values(downloads.downloads).length;
		if (len === 0) {
			return undefined;
		}
		return len >= 99 ? '99+' : `${len}`;
	});
</script>

<Collapsible.Root open={true}>
	{#snippet child({ props })}
		<Sidebar.MenuItem {...props}>
			<Sidebar.MenuButton tooltipContent={item.title} isActive={page.route.id === item.url}>
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
						{#if !sidebar.open && count}
							<span class="absolute -top-1 -right-1">
								<Badge variant="outline" class="h-4 min-w-4 px-1 text-[10px]">
									{count}
								</Badge>
							</span>
						{/if}
					</a>
					<!-- eslint-enable svelte/no-navigation-without-resolve -->
				{/snippet}
			</Sidebar.MenuButton>
			{#if count}
				<Sidebar.MenuBadge class={badgeVariants({ variant: 'outline' })}>{count}</Sidebar.MenuBadge>
			{/if}
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
								<Sidebar.MenuSubButton href={subItem.url} isActive={page.route.id === subItem.url}>
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
