
<script>
    let planets = [];

    // Fetch from your Flask API
    async function loadPlanets() {
        const res = await fetch('http://localhost:5000/api/planets'); // Update URL if needed
        planets = await res.json();
    }

    loadPlanets();
</script>

<style>
    .planet-card {
        border: 1px solid #ccc;
        border-radius: 1rem;
        padding: 1rem;
        margin: 1rem 0;
        max-width: 500px;
        background-color: #070516;
        color: white;
    }

    img {
        max-width: 100%;
        border-radius: 0.5rem;
    }
</style>

<h1> Welcome to StarBNB! </h1>
<p>Explore habitable planets to visit or terraform while on your dream vacation across the stars.</p>

{#each planets as planet}
    <div class="planet-card">
        <h2>{planet.name}</h2>
        <img src={planet.image_url} alt={planet.name} />
        <p>{planet.description}</p>
        <p><strong>Distance:</strong> {planet.distance_light_years} light-years</p>
        <p><strong>Gravity:</strong> {planet.gravity.toFixed(2)} m/s²</p>
        <p><strong>Travel Time:</strong> {planet.travel_time.toFixed(2)} years</p>
        <p><strong>Time Gained:</strong> {planet.time_gained.toFixed(2)} years</p>
        <p><strong>Price:</strong> ${planet.price_per_night}</p>
    </div>
{/each}
