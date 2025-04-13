<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>StarBnB - Your Galactic Getaway</title>
  <style>
    /* Galactic Getaway Color Palette */
    :root {
        --dark-space: #0C2A4D; /* Deep space blue */
        --nebula-purple: #4A148C; /* Nebula purple */
        --starlight-yellow: #FFDB58; /* Starlight yellow */
        --planet-gray: #F1F3F5; /* Planet surface gray */
        --button-blue: #007bff; /* Button blue */
        --button-hover: #0056b3; /* Button hover blue */
    }

    body {
        margin: 0;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
        background: linear-gradient(to bottom, var(--dark-space), var(--nebula-purple));
        color: var(--planet-gray);
        text-align: center;
    }

    header {
        padding: 50px;
    }

    h1 {
        font-size: 3rem;
        color: var(--starlight-yellow);
    }

    h2 {
        font-size: 1.5rem;
        margin-top: 10px;
    }

    a {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        gap: 8px;
        margin-top: 20px;
        padding: 10px 20px;
        background-color: var(--button-blue);
        color: white;
        text-decoration: none;
        border-radius: 5px;
        font-size: 1rem;
    }

    a:hover {
        background-color: var(--button-hover);
    }

    .material-symbols-outlined {
        font-size: 1.2rem;
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

  <!-- Include Google Material Symbols -->
  <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined" rel="stylesheet" />
</head>
<body>
  <script>
    export let name = "StarBnB"; 
    export let tagline = "Your Galactic Getaway In The Stars Awaits!";
    export let buttonText = "Explore Here";
    export let planets = []; // Placeholder for planets data
    export let filter = 'all'; // Default filter value
  </script>

  <main>
    <header>
      <h1>{name}</h1>
      <h2>{tagline}</h2>
      <a href="/featured">
        <span class="material-symbols-outlined">travel_explore</span>
        {buttonText}
      </a>
    </header>
  </main>

  <section class="destinations">
    <div class="card">
      <div class="icon">🪐</div>
      <h3>Planets</h3>
      <p>Explore exotic worlds across the galaxy.</p>
    </div>
    <div class="card">
      <div class="icon">🌕</div>
      <h3>Moons</h3>
      <p>Stay on serene moons with stellar views.</p>
    </div>
    <div class="card">
      <div class="icon">🛰️</div>
      <h3>Orbitals</h3>
      <p>Book luxury stays on futuristic space stations.</p>
    </div>
  </section>
</body>
</html>