<script>
    import { onMount } from 'svelte';

    let planets = [];
    let filter = 'all';

     // Fetch planets from Flask API

    onMount(async () => {
        const res = await fetch('http://127.0.0.1:5000/query=GET extract'); // Adjust if needed
        planets = await res.json();
        console.log(planets);
	});

    function filteredPlanets() {
        if (filter === 'all') return planets;
        return planets.filter(p => p.type === filter);
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

    img {
        max-width: 100%;
        border-radius: 0.5rem;
    }

    select {
        margin: 1rem 0;
        padding: 0.5rem;
        border-radius: 0.5rem;
    }
</style>



<h1>Time to Explore Your Planet Options!</h1>

<select bind:value={filter}>
    <option value="all">All</option>
    <option value="habitable">Habitable</option>
</select>

<div class="planet-grid">
    {#each filteredPlanets() as planet}
        <div class="planet-card">
            <h2>{planet.name}</h2>
            <img src={planet.image_url} alt={planet.name} />
            <p>{planet.description}</p>
            <p><strong>Type:</strong> {planet.type}</p>
            <p><strong>Distance:</strong> {planet.distance_light_years} light-years</p>
            <p><strong>Gravity:</strong> {planet.gravity.toFixed(2)} m/s²</p>
            <p><strong>Travel Time:</strong> {planet.travel_time.toFixed(2)} years</p>
            <p><strong>Time Gained:</strong> {planet.time_gained.toFixed(2)} years</p>
            <p><strong>Price:</strong> ${planet.price_per_night}</p>
        </div>
    {/each}
</div>
