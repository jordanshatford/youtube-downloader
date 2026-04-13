<script lang="ts">
	import { versions } from '$lib/stores/versions.svelte';

	import { Table, Tabs } from '@yd/ui';
</script>

<Tabs.Content value="/settings/versions">
	<Table.Root>
		<Table.Caption>A list of relevant versions.</Table.Caption>
		<Table.Header>
			<Table.Row>
				<Table.Head>Component</Table.Head>
				<Table.Head class="text-end">Version</Table.Head>
			</Table.Row>
		</Table.Header>
		<Table.Body>
			{#each versions.items as item (item.component)}
				<Table.Row>
					<Table.Cell class="font-medium">{item.component}</Table.Cell>
					<Table.Cell class="text-end">
						<code
							class="bg-muted relative rounded px-[0.3rem] py-[0.2rem] font-mono text-sm font-semibold"
						>
							{item.version}
						</code>
					</Table.Cell>
				</Table.Row>
			{/each}
		</Table.Body>
	</Table.Root>
</Tabs.Content>
