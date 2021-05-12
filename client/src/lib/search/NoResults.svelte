<script lang="ts">
    import Icon from "../Icon.svelte"
    import Description from "../typography/Description.svelte"
    import { search } from "../icons"
</script>

<div class="inline-block relative w-100 overflow-hidden align-middle m-auto text-center">
    <Icon data={search} size={3} className="text-gray-900 dark:text-gray-100" />
    <Description>No results found!</Description>
</div>