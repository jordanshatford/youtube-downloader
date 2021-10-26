<script lang="ts">
	import Icon from '$lib/components/Icon.svelte'
	import Description from '$lib/components/typography/Description.svelte'
	import { search } from '$lib/components/icons'
</script>

<div class="inline-block relative w-100 overflow-hidden align-middle m-auto text-center">
	<Icon data={search} size={3} className="text-gray-900 dark:text-gray-100" />
	<Description>No results found!</Description>
</div>
