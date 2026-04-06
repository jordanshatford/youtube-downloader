<script lang="ts">
	import { page } from '$app/state';
	import { routeNamesLong } from '$lib/routes';

	import { Breadcrumb } from '@yd/ui';
</script>

<Breadcrumb.Root>
	<Breadcrumb.List>
		<Breadcrumb.Item>
			<Breadcrumb.Page>{page.route.id ? routeNamesLong[page.route.id] : ''}</Breadcrumb.Page>
		</Breadcrumb.Item>
	</Breadcrumb.List>
</Breadcrumb.Root>
