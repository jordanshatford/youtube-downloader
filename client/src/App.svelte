<script>
	export let name;

	let rand = -1
	function getRand() {
    fetch("./rand")
      .then(d => d.text())
      .then(d => (rand = d));
  	}
</script>

<main>
	<h1>Hello {name}!</h1>
	<p>Visit the <a href="https://svelte.dev/tutorial">Svelte tutorial</a> to learn how to build Svelte apps.</p>

	<h1>Your number is {rand}!</h1>
	<button class="bg-blue-500 hover:bg-blue-700 text-white outline:none font-bold py-2 px-4 rounded" on:click={getRand}>Get a random number</button>
</main>

<style global>
	@tailwind base;
	@tailwind components;
	@tailwind utilities;
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>