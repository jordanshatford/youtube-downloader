<script lang="ts">
	export let className = ''
	export let size = 1
	export let data: string
</script>

<svg
	class="{className} relative inline-block"
	viewBox="0 0 24 24"
	fill="none"
	width={`${size}rem`}
	height={`${size}rem`}
	xmlns="http://www.w3.org/2000/svg"
>
	<path
		d={data}
		stroke="#4A5568"
		class="stroke-current"
		stroke-width="2"
		stroke-linecap="round"
		stroke-linejoin="round"
	/>
</svg>
