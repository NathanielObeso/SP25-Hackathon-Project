<script>
    import { onMount } from 'svelte';

    let planets = [];
    let terraform_planets = [];
    let filter = '';

     // Fetch planets from Flask API

    onMount(async () => {
        const res = await fetch('http://127.0.0.1:5000/extract'); // Adjust if needed
        planets = await res.json();
        const res2 = await fetch('http://127.0.0.1:5000/api/terraforming');
        terraform_planets = await res2.json()
	});

    function filteredPlanets() {
        if (filter === 'all') return planets;
        else if (filter === 'uninhabitable') return terraform_planets;
        return planets.filter(p => p.category === filter);
    }
</script>

<style>
    .planet-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 1rem;
        padding: 1rem;
    }

    .planet-card {
        background-color: #0C2A4D;
        color: white;
        border-radius: 1rem;
        padding: 1rem;
        box-shadow: 0 0 12px rgba(0, 0, 0, 0.4);
        transition: transform 0.2s ease;
    }

    .planet-card:hover {
        transform: scale(1.03);
    }

    select {
        margin: 1rem 0;
        padding: 0.5rem;
        border-radius: 0.5rem;
    }


</style>



<h1>Time to Explore Your Planet Options!</h1>

<select bind:value={filter}>
    <option value=""></option>
    <option value="all">All</option>
    <option value="habitable">Habitable</option>
    <option value="uninhabitable">Uninhabitable</option>
</select>

<!-- Grid to display planets -->
<div class="planet-grid">
    {#each filteredPlanets() as planet}
        <div class="planet-card">
            <h2>{planet.pl_name}</h2>
            <p><strong>Distance:</strong> {planet.distance_light_years} light-years</p>
            <p><strong>Orbit Period:</strong> {planet.pl_orblper} days</p>
            <p><strong>Gravity:</strong> {planet.gravity} m/s²</p>
            <p><strong>Radius:</strong> {planet.pl_rade} Earth radii</p>
            <p><strong>Category:</strong> {planet.category}</p>
        </div>
    {/each}
</div>

