<script lang="ts">
	import type { VideoInfo } from "../../utils/types"
    import ResultCard from "./ResultCard.svelte"

    export let results: VideoInfo[]
</script> 


<div class="container mt-8 pb-8 mx-auto px-4 md:px-12">
    <div class="flex flex-wrap -mx-1 lg:-mx-4">
        {#each results as result (result.id)}
            <ResultCard result={result} />
        {/each}
    </div>
</div>
