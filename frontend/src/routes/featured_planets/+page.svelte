<script>
    import { onMount } from 'svelte';

    let planets = [];
    let terraform_planets = [];
    let filter = '';

     // Fetch planets from Flask API

    onMount(async () => {
<<<<<<< HEAD
        const res = await fetch('http://127.0.0.1:5000/extract'); // Adjust if needed
        planets = await res.json();
        const res2 = await fetch('http://127.0.0.1:5000/api/terraforming');
        terraform_planets = await res2.json()
=======
        const res = await fetch('http://localhost:5000/test_planets'); // Adjust the URL if needed
        const data = await res.json();
        console.log(data)
        planets = data.planets; // Assign the fetched planets to the variable
>>>>>>> 86aaed8cea6c11bb35f74d7e2151830f8e7951a5
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
<<<<<<< HEAD
=======
    <option value="terraforming">Terraforming</option>
>>>>>>> 86aaed8cea6c11bb35f74d7e2151830f8e7951a5
</select>

<!-- Grid to display planets -->
<div class="planet-grid">
    {#each planets as planet}
        <div class="planet-card">
            <h2>{planet.pl_name}</h2>
<<<<<<< HEAD
            <!-- img src={planet.image_url} alt={planet.name} /-->
            <!--<p>{planet.description}</p>-->
            <!--<p><strong>Type:</strong> {planet.type}</p>-->
            <p><strong>Distance:</strong> {planet.distance_light_years} light-years</p>
            <p><strong>Gravity:</strong> {planet.gravity.toFixed(2)} m/s²</p>
            <!--<p><strong>Travel Time:</strong> {planet.travel_time.toFixed(2)} years</p>-->
            <!--<p><strong>Time Gained:</strong> {planet.time_gained.toFixed(2)} years</p>-->
            <!--<p><strong>Price:</strong> ${planet.price_per_night}</p>-->
=======
            <p><strong>Distance:</strong> {planet.distance_light_years} light-years</p>
            <p><strong>Orbit Period:</strong> {planet.pl_orblper} days</p>
            <p><strong>Gravity:</strong> {planet.gravity} m/s²</p>
            <p><strong>Radius:</strong> {planet.pl_rade} Earth radii</p>
            <p><strong>Category:</strong> {planet.category}</p>
>>>>>>> 86aaed8cea6c11bb35f74d7e2151830f8e7951a5
        </div>
    {/each}
</div>

