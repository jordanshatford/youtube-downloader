<script lang="ts">
  import IconButton from "../lib/IconButton.svelte"
  import { theme } from "../../stores/theme"
  import { moonO, sunO } from "svelte-awesome/icons"

  function toggleTheme() {
    $theme = $theme === "dark" ? "light" : "dark"
    document.querySelector("html").classList.toggle("dark")
  }
</script>

<IconButton
    on:click={toggleTheme}
    data={$theme === "dark" ? sunO : moonO}
    className="text-gray-500 dark:text-gray-200 dark:bg-gray-900 hover:bg-gray-50 dark:hover:bg-gray-800 hover:text-gray-700"
    scale={1.5}
/>
