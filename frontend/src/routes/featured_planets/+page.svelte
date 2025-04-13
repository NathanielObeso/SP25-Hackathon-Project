<script>
    import { onMount } from 'svelte';

    let planets = [];
    let filter = 'all';

     // Fetch planets from Flask API

    onMount(async () => {
        const res = await fetch('http://localhost:5000/test_planets'); // Adjust the URL if needed
        const data = await res.json();
        console.log(data)
        planets = data.planets; // Assign the fetched planets to the variable
	});

    function filteredPlanets() {
        if (filter === 'all') return planets;
        return planets.filter(p => p.category === filter); // Filter by category
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
        background-color: #111;
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

<!-- Dropdown to filter planets -->
<select bind:value={filter}>
    <option value="all">All</option>
    <option value="habitable">Habitable</option>
    <option value="uninhabitable">Uninhabitable</option>
    <option value="terraforming">Terraforming</option>
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

