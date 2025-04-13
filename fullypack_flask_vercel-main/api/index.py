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

def store_planets_in_db(planets):
    for planet in planets:
        c.execute('INSERT INTO habitable_planets VALUES (?, ?, ?, ?, ?)', (
            planet['pl_name'],
            planet['distance_light_years'],
            planet['pl_orblper'],
            planet['gravity'],
            planet['pl_rade']
        ))
    conn.commit()

# Fetch and store the data
habitable_planets = get_exoplanet_data(habitable_query)
if habitable_planets:
    store_planets_in_db(habitable_planets)

@app.route('/')
@app.route('/index')
def index():
    # Query to fetch habitable planets
    habitable_query = """
        SELECT TOP 30 pl_name, sy_dist * 3.26156 AS distance_light_years, pl_orblper, 
        (pl_massj * 317.83) / POWER(pl_rade, 2) AS gravity, pl_rade 
        FROM ps 
        WHERE sy_dist IS NOT NULL AND pl_rade IS NOT NULL 
        AND pl_orblper >= 365.25 * 0.8 AND pl_orblper <= 365.25 * 1.2 
        ORDER BY sy_dist;
    """
    # Fetch data from NASA's API
    url = f"https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query={habitable_query}&format=json"
    response = requests.get(url)
    planets = response.json() if response.status_code == 200 else []

    # Pass the data to the frontend
    return render_template('index.html', planets=planets)

@app.route('/planets', methods=['GET'])
def get_planets():
    c.execute('SELECT * FROM habitable_planets')
    planets = c.fetchall()
    return {"planets": planets}

@app.route('/<path:path>')
def catch_all(path):
    """A special route that catches all other requests

    Note: Let this be your last route. Priority is defined
    by order, so placing this above other functions will
    cause catch_all() to override then.

    Return: A redirect to our index route
    """

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
