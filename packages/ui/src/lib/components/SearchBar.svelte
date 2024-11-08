<script lang="ts">
	import { Icon, LoaderIcon, MagnifyingGlassIcon } from '../icons';

	interface Props {
		loading?: boolean;
		query: string;
		onsearch: (query: string) => void;
	}

	let { loading = false, query = $bindable(), onsearch }: Props = $props();

	function search(event: KeyboardEvent) {
		if (event.key === 'Enter' && query.length > 0) {
			onsearch(query);
		}
	}
</script>

<div class="w-full">
	<div class="flex">
		<div class="pointer-events-none z-10 flex w-10 items-center justify-center pl-1 text-center">
			<Icon
				src={loading ? LoaderIcon : MagnifyingGlassIcon}
				class="h-5 w-5 text-zinc-400 {loading && 'animate-spin'}"
			/>
		</div>
		<input
			id="search"
			disabled={loading}
			bind:value={query}
			onkeypress={search}
			type="search"
			class="-ml-10 w-full rounded-lg border-2 border-zinc-200 py-2 pl-10 pr-3 text-zinc-600 outline-none focus:border-brand-600 focus:ring-transparent dark:border-zinc-600 dark:bg-zinc-800 dark:text-zinc-200 dark:focus:border-brand-600 dark:disabled:bg-zinc-600"
			placeholder="search"
		/>
	</div>
</div>
