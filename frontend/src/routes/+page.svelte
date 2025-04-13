

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>StarBnB - Galactic Getaway</title>
  <style>

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


  .explore-btn {
    display: inline-block;
    margin-top: 2rem;
    padding: 1rem 2rem;
    background-color: #0C2A4D;
    color: white;
    font-weight: bold;
    text-decoration: none;
    border-radius: 0.75rem;
    box-shadow: 0 0 12px rgba(0,0,0,0.3);
    transition: background-color 0.3s ease;
  }

  .explore-btn:hover {
    background-color: #9067C6;
  }

  </style>
</head>

<body>
  <header>
    <h1>✦ StarBnB ✦</h1>
    <h2>⁂ Your Galactic Getaway In The Stars Awaits! ⁂</h2>
    <a href="/featured_planets" class="explore-btn">🌍 Explore Featured Planets Here!</a>
  </header>

  <section class="destinations">
    <div class="card">
      <div class="icon">🪐</div>
      <h3>Planets</h3>
      <p>Explore exotic worlds across the galaxy.</p>
    </div>
  </section>
</body>
</html>