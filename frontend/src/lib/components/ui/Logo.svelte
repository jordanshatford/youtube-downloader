<script lang="ts">
	import { goto } from '$app/navigation'
	import { RoutePathConstants } from '$lib/utils/RouteUtils'
</script>

<button class="focus:outline-none" on:click={() => goto(RoutePathConstants.SEARCH)}>
	<img class="block h-8 w-auto" src="images/logo.png" alt="Logo" />
</button>
