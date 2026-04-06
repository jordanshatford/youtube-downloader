<script lang="ts" module>
	import { resolve } from '$app/paths';

	import { ArrowUpRightIcon, BanIcon, Button, Empty } from '@yd/ui';
</script>

<Empty.Root>
	<Empty.Header>
		<Empty.Media variant="icon">
			<BanIcon />
		</Empty.Media>
		<Empty.Title>Not found.</Empty.Title>
		<Empty.Description>
			The page you are looking for could not be found. It may have been removed or is temporarily
			unavailable. Please check the URL and try again.
		</Empty.Description>
	</Empty.Header>
	<Empty.Content>
		<div class="flex gap-2">
			<Button.Root variant="link" class="text-muted-foreground" size="sm">
				<a href={resolve('/')}>
					Home <ArrowUpRightIcon class="inline" />
				</a>
			</Button.Root>
		</div>
	</Empty.Content>
</Empty.Root>
