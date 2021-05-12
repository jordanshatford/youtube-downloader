<script lang="ts">
  import IconButton from "../IconButton.svelte"
  import { theme } from "../../stores/theme"
  import { moon, sun } from "../icons"
</script>

<IconButton
    on:click={_ => theme.toggle()}
    data={$theme === "dark" ? sun : moon}
    className="text-gray-500 dark:text-gray-200 dark:bg-gray-900 hover:bg-gray-50 dark:hover:bg-gray-800 hover:text-gray-700"
    size={1.5}
/>
