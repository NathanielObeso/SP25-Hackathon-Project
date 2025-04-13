<script>
  export let name = "StarBnB"; 
  export let tagline = "Your Galactic Getaway In The Stars Awaits!";
  export let buttonText = "Explore Here";
  export let planets = []; // Placeholder for planets data
  export let filter = 'all'; // Default filter value
</script>


<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>StarBnB - Galactic Getaway</title>
<style>
  body {
    margin: 0;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: linear-gradient(to bottom, #0C2A4D, #4A148C);
    color: #F1F3F5;
    text-align: center;
  }

  header {
    padding: 3rem 1rem 2rem;
  }

  header h1 {
    font-size: 3rem;
    margin: 0;
    color: #FFDB58;
  }

  header h2 {
    font-size: 1.5rem;
    margin: 0.5rem 0 2rem;
  }
.\<env_name>\Scripts\activate
  .button {
    background-color: #9067C6;
    color: white;
    border: none;
    border-radius: 0.5rem;
    padding: 1rem 2rem;
    font-size: 1rem;
    cursor: pointer;
    transition: background 0.3s ease;
  }

  .button:hover {
    background-color: #4A148C;
  }

  .destinations {
    display: flex;
    justify-content: center;
    gap: 1rem;
    margin-top: 4rem;
    flex-wrap: wrap;
  }

  .card {
    background: #1b1b2f;
    border-radius: 1rem;
    width: 200px;
    padding: 1.5rem 1rem;
    color: #F1F3F5;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);
  }

  .card h3 {
    margin: 1rem 0 0.5rem;
    font-size: 1.2rem;
  }

  .icon {
    font-size: 3rem;
    margin-bottom: 0.5rem;
  }
</style>
</head>
<body>
<header>
  <h1>✦ StarBnB ✦</h1>
  <h2>⁂ Your Galactic Getaway In The Stars Awaits! ⁂</h2>
  <button class="button">Explore Here</button>
</header>

<section class="destinations">
  <div class="card">
    <div class="icon">🪐</div>
    <h3>Planets</h3>
    <p>Explore exotic worlds across the galaxy.</p>
  </div>
  <!-- Future Destination Options, show when implemented
    <div class="card">
    <div class="icon">🌕</div>
    <h3>Moons</h3>
    <p>Stay on serene moons with stellar views.</p>
  </div>
  <div class="card">
    <div class="icon">🛰️</div>
    <h3>Orbitals</h3>
    <p>Book luxury stays on futuristic space stations.</p>
  </div>-->
</section>
</body>
</html>