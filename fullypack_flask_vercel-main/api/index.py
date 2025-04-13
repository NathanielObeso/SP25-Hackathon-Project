from flask import Flask, redirect, url_for, render_template, request
import requests
import json
import sqlite3

# Our Flask app object
app = Flask(__name__, template_folder='../templates',
            static_folder='../static')

@app.route('/extract', methods=['GET'])
def get_exoplanet_data():
    query = request.args.get('query')  # Get the query from the request
    url = f"https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query={query}&format=json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to fetch data from NASA"}

habitable_query = "SELECT TOP 30 pl_name, sy_dist * 3.26156 AS distance_light_years, pl_orblper, (pl_massj * 317.83) / POWER(pl_rade, 2) AS gravity, pl_rade, pl_orbper FROM ps WHERE sy_dist IS NOT NULL AND pl_rade IS NOT NULL AND pl_massj IS NOT NULL AND pl_orblper >= 365.25 * 0.8 AND pl_orblper <= 365.25 * 1.2 ORDER BY sy_dist ASC;"
habitable_planets = get_exoplanet_data(habitable_query)

for planet in habitable_planets:
    print(f'{planet['pl_name']}: {planet['distance_light_years']} light years, Orbital period of {planet['pl_orblper']} days, gravity of {planet['gravity']}, radius of {planet['pl_rade']} Earth radii, {planet['pl_orbper']} days to orbit')

terraform_query = "SELECT TOP 30 pl_name, sy_dist*3.26156 AS distance_light_years, pl_rade, pl_massj, pl_eqt FROM ps WHERE pl_rade > 1 AND pl_massj < 10 AND pl_eqt > 100 AND pl_eqt < 400 ORDER BY sy_dist ASC;"
terraforming_planets = get_exoplanet_data(terraform_query)
# Fetch and store the data in memory
habitable_query = "SELECT TOP 30 pl_name, sy_dist * 3.26156 AS distance_light_years, pl_orblper, (pl_massj * 317.83) / POWER(pl_rade, 2) AS gravity, pl_rade FROM ps WHERE sy_dist IS NOT NULL AND pl_rade IS NOT NULL AND pl_orblper >= 365.25 * 0.8 AND pl_orblper <= 365.25 * 1.2 ORDER BY sy_dist;"

# Create a database connection
conn = sqlite3.connect('planets.db')
c = conn.cursor()

# Create a table for habitable planets
c.execute('''CREATE TABLE IF NOT EXISTS habitable_planets (
    pl_name TEXT,
    distance_light_years REAL,
    pl_orblper REAL,
    gravity REAL,
    pl_rade REAL
)''')
conn.commit()

c.execute('''CREATE TABLE IF NOT EXISTS planets (
    pl_name TEXT,
    distance_light_years REAL,
    pl_orblper REAL,
    gravity REAL,
    pl_rade REAL,
    category TEXT
)''')
conn.commit()

def store_planets_in_db(planets, category):
    for planet in planets:
        c.execute('INSERT INTO planets VALUES (?, ?, ?, ?, ?, ?)', (
            planet['pl_name'],
            planet['distance_light_years'],
            planet['pl_orblper'],
            planet['gravity'],
            planet['pl_rade'],
            category
        ))
    conn.commit()

def get_db_connection():
    conn = sqlite3.connect('planets.db')
    conn.row_factory = sqlite3.Row  # Optional: Return rows as dictionaries
    return conn

def fetch_data_from_nasa(query):
    url = f"https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query={query}&format=json"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return []

@app.route('/index')
def index():
    habitable_query = """
        SELECT TOP 30 pl_name, sy_dist * 3.26156 AS distance_light_years, pl_orblper, 
        (pl_massj * 317.83) / POWER(pl_rade, 2) AS gravity, pl_rade 
        FROM ps 
        WHERE sy_dist IS NOT NULL AND pl_rade IS NOT NULL 
        AND pl_orblper >= 365.25 * 0.8 AND pl_orblper <= 365.25 * 1.2 
        ORDER BY sy_dist;
    """
    terraforming_query = """
        SELECT TOP 30 pl_name, sy_dist * 3.26156 AS distance_light_years, pl_orblper, 
        (pl_massj * 317.83) / POWER(pl_rade, 2) AS gravity, pl_rade 
        FROM ps 
        WHERE sy_dist IS NOT NULL AND pl_rade IS NOT NULL 
        AND pl_orblper > 365.25 * 1.2 
        ORDER BY sy_dist;
    """

    habitable_planets = fetch_data_from_nasa(habitable_query)
    terraforming_planets = fetch_data_from_nasa(terraforming_query)

    return render_template('index.html', habitable_planets=habitable_planets, terraforming_planets=terraforming_planets)

@app.route('/planets', methods=['GET'])
def get_planets():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('SELECT * FROM habitable_planets')
    planets = c.fetchall()
    conn.close()
    return {"planets": planets}

@app.route('/<path:path>')
def catch_all(path):
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

import requests

query = """
    SELECT TOP 30 pl_name, sy_dist * 3.26156 AS distance_light_years, pl_orblper, 
    (pl_massj * 317.83) / POWER(pl_rade, 2) AS gravity, pl_rade 
    FROM ps 
    WHERE sy_dist IS NOT NULL AND pl_rade IS NOT NULL 
    AND pl_orblper >= 365.25 * 0.8 AND pl_orblper <= 365.25 * 1.2 
    ORDER BY sy_dist;
"""
url = f"https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query={query}&format=json"
response = requests.get(url)
print(response.json())
