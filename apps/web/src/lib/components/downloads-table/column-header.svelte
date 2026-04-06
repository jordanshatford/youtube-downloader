<script lang="ts">
	import type { HTMLAttributes } from 'svelte/elements';

	import type { Download } from '@yd/client';
	import type { Column } from '@yd/ui';
	import {
		ArrowDownIcon,
		ArrowUpIcon,
		Button,
		ChevronsUpDownIcon,
		cn,
		DropdownMenu,
		EyeOffIcon
	} from '@yd/ui';

	let {
		column,
		title,
		class: className,
		...restProps
	}: { column: Column<Download>; title: string } & HTMLAttributes<HTMLDivElement> = $props();
</script>

{#if !column?.getCanSort()}
	<div class={className} {...restProps}>
		{title}
	</div>
{:else}
	<div class={cn('flex items-center', className)} {...restProps}>
		<DropdownMenu.Root>
			<DropdownMenu.Trigger>
				{#snippet child({ props })}
					<Button.Root
						{...props}
						variant="ghost"
						size="sm"
						class="data-[state=open]:bg-accent -ms-3 h-8"
					>
						<span>
							{title}
						</span>
						{#if column.getIsSorted() === 'desc'}
							<ArrowDownIcon />
						{:else if column.getIsSorted() === 'asc'}
							<ArrowUpIcon />
						{:else}
							<ChevronsUpDownIcon />
						{/if}
					</Button.Root>
				{/snippet}
			</DropdownMenu.Trigger>
			<DropdownMenu.Content align="start">
				<DropdownMenu.Item onclick={() => column.toggleSorting(false)}>
					<ArrowUpIcon class="text-muted-foreground/70 me-2 size-3.5" />
					Asc
				</DropdownMenu.Item>
				<DropdownMenu.Item onclick={() => column.toggleSorting(true)}>
					<ArrowDownIcon class="text-muted-foreground/70 me-2 size-3.5" />
					Desc
				</DropdownMenu.Item>
				{#if column?.getCanHide()}
					<DropdownMenu.Separator />
					<DropdownMenu.Item onclick={() => column.toggleVisibility(false)}>
						<EyeOffIcon class="text-muted-foreground/70 me-2 size-3.5" />
						Hide
					</DropdownMenu.Item>
				{/if}
			</DropdownMenu.Content>
		</DropdownMenu.Root>
	</div>
{/if}
