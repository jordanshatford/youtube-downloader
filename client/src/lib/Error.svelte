<script lang="ts">
    export let code: string = ""
    export let description: string = ""
</script>

<div class="bg-white dark:bg-gray-900">
	<div class="flex h-screen">
		<div class="m-auto text-center">
			<div class="inline-block relative w-100 overflow-hidden align-middle">
				<div class="text-gray-900 dark:text-white">
					<h1 class="text-9xl">{code}</h1>
					<h2 class="text-xl mt-2">{description}</h2>
				</div>
                <div>
                    <slot name="actions" />
                </div>
			</div>
		</div>
	</div>
</div>