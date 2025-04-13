from flask import Flask, redirect, url_for, render_template, request
from flask_cors import CORS
import json
import sqlite3
from flask_cors import CORS

# Our Flask app object
app = Flask(__name__, template_folder='../templates',
            static_folder='../static')
CORS(app)
#
test_planets = [
    {
        "pl_name": "Test Earth",
        "distance_light_years": 0.0,
        "pl_orblper": 365.25,
        "gravity": 9.8,
        "pl_rade": 1.0,
        "category": "habitable"
    },
    {
        "pl_name": "Mars",
        "distance_light_years": 0.0000158,
        "pl_orblper": 687.0,
        "gravity": 3.7,
        "pl_rade": 0.53,
        "category": "habitable"
    },
    {
        "pl_name": "Venus",
        "distance_light_years": 0.0000114,
        "pl_orblper": 225.0,
        "gravity": 8.87,
        "pl_rade": 0.95,
        "category": "uninhabitable"
    },
    {
        "pl_name": "Proxima b",
        "distance_light_years": 4.24,
        "pl_orblper": 11.2,
        "gravity": 11.0,
        "pl_rade": 1.1,
        "category": "habitable"
    },
    {
        "pl_name": "Kepler-452b",
        "distance_light_years": 1400.0,
        "pl_orblper": 385.0,
        "gravity": 19.6,
        "pl_rade": 1.63,
        "category": "habitable"
    },
    {
        "pl_name": "Kepler-22b",
        "distance_light_years": 600.0,
        "pl_orblper": 290.0,
        "gravity": 15.0,
        "pl_rade": 2.4,
        "category": "terraforming"
    }
]

def store_test_planets_in_db(test_planets):
    # Connect to the SQLite database
    conn = sqlite3.connect('planets.db')
    c = conn.cursor()

    # Iterate through the list of planets and insert them into the database
    for planet in test_planets:
        c.execute('''
            INSERT INTO planets (pl_name, distance_light_years, pl_orblper, gravity, pl_rade, category)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (
            planet['pl_name'],
            planet['distance_light_years'],
            planet['pl_orblper'],
            planet['gravity'],
            planet['pl_rade'],
            planet['category']
        ))

    # Commit the transaction and close the connection
    conn.commit()
    conn.close()

@app.route('/test_planets', methods=['GET'])
def get_test_planets():
    return {"planets": test_planets}

#

import requests


@app.route('/extract', methods=['GET'])
def get_exoplanet_data():
    query = "SELECT TOP 30 pl_name, sy_dist * 3.26156 AS distance_light_years, pl_orblper, (pl_massj * 317.83) / POWER(pl_rade, 2) AS gravity, pl_rade, pl_orbper FROM ps WHERE sy_dist IS NOT NULL AND pl_rade IS NOT NULL AND pl_massj IS NOT NULL AND pl_orblper >= 365.25 * 0.8 AND pl_orblper <= 365.25 * 1.2 ORDER BY sy_dist;"  # Get the query from the request
    url = f"https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query={query}&format=json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to fetch data from NASA"}
    
@app.route('/api/terraforming', methods=['GET'])
def get_terraform_data():
    query = "SELECT TOP 30 pl_name, sy_dist*3.26156 AS distance_light_years, pl_rade, pl_massj, pl_eqt, (pl_massj * 317.83) / POWER(pl_rade, 2) AS gravity FROM ps WHERE pl_rade > 1 AND pl_massj < 10 AND pl_eqt > 100 AND pl_eqt < 400 AND pl_massj IS NOT NULL AND pl_rade IS NOT NULL ORDER BY sy_dist ASC;"  # Get the query from the request
    url = f"https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query={query}&format=json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to fetch data from NASA"}
    
# Fetch and store the data in memory
#habitable_query = "SELECT TOP 30 pl_name, sy_dist * 3.26156 AS distance_light_years, pl_orblper, (pl_massj * 317.83) / POWER(pl_rade, 2) AS gravity, pl_rade, pl_orbper FROM ps WHERE sy_dist IS NOT NULL AND pl_rade IS NOT NULL AND pl_orblper >= 365.25 * 0.8 AND pl_orblper <= 365.25 * 1.2 ORDER BY sy_dist;"
#habitable_planets = get_exoplanet_data(habitable_query)

#for planet in habitable_planets:
    #print(f'{planet['pl_name']}: {planet['distance_light_years']} light years, Orbital period of {planet['pl_orblper']} days, gravity of {planet['gravity']}, radius of {planet['pl_rade']} Earth radii, {planet['pl_orbper']} days to orbit')

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