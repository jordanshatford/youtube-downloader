<script lang="ts">
	import { onMount } from 'svelte';
	import { goto } from '$app/navigation';
	import { RoutePathConstants } from '$lib/utils/route';
	onMount(() => goto(RoutePathConstants.SEARCH));
</script>
