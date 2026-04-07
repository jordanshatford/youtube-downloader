<script lang="ts">
	import { page } from '$app/state';
	import { routes } from '$lib/routes';

	import { Breadcrumb } from '@yd/ui';

	let current = $derived(page.route.id);
	const items = [...routes.main, ...routes.footer].filter((r) => !r.external);

	let crumbs = $derived.by(() => {
		for (let item of items) {
			const crumb = item.titleLong ?? item.title;
			if (item.url === current) {
				return [crumb];
			}

			const subitems = item.items ?? [];
			for (let subitem of subitems) {
				if (subitem.url === current) {
					const subcrumb = subitem.titleLong ?? subitem.title;
					return [crumb, subcrumb];
				}
			}
		}
		return [];
	});
</script>

<Breadcrumb.Root>
	<Breadcrumb.List>
		<Breadcrumb.Item>
			{#each crumbs as crumb, i (crumb)}
				<Breadcrumb.Page>{crumb}</Breadcrumb.Page>
				{#if i < crumbs.length - 1}
					<Breadcrumb.Separator />
				{/if}
			{/each}
		</Breadcrumb.Item>
	</Breadcrumb.List>
</Breadcrumb.Root>
