<script lang="ts">
	import type { SearchResult } from "../../utils/types"
    import ResultCard from "./ResultCard.svelte"
    export let results: SearchResult[]
</script> 


<div class="container my-12 mx-auto px-4 md:px-12">
    <div class="flex flex-wrap -mx-1 lg:-mx-4">
        {#each results as result (result.webpage_url)}
            <ResultCard result={result} />
        {/each}
    </div>
</div>
