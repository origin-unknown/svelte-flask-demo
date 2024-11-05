<script>
	import { onMount } from 'svelte';

	let rand = $state(-1);

	function getRand() {
		fetch('/api/rand')
			.then(d => d.text())
			.then(d => (rand = d));
	}

	onMount(getRand)
</script>

<h1>Your number is {rand}!</h1>
<button onclick={getRand}>Get a random number</button>