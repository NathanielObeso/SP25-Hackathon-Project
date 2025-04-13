<script>
    // This will expose the content from child pages
    export let data;
  </script>
  
  <style>
    :global(body) {
      margin: 0;
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      background: linear-gradient(to bottom, #0C2A4D, #4A148C);
      color: #F1F3F5;
      text-align: center;
    }
  
    main {
      max-width: 1200px;
      margin: 0 auto;
      padding: 2rem;
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
  
    nav a {
      color: white;
      margin-right: 1rem;
      text-decoration: none;
      font-weight: bold;
    }
  
    nav a:hover {
      text-decoration: underline;
    }
  </style>
  
  <header>
    <h1>🚀 StarBNB</h1>
    <nav>
      <a href="/">Home</a>
      <a href="/featured_planets">Featured Planets</a>
      <!-- Add more nav links here -->
    </nav>
  </header>
  
  <main>
    <slot /> <!-- This is where the current page content renders -->
  </main>