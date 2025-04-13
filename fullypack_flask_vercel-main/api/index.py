from flask import Flask, redirect, url_for, render_template
import requests
import json

# Our Flask app object
app = Flask(__name__, template_folder='../templates',
            static_folder='../static')

@app.route('/extract', methods=['GET'])
def get_exoplanet_data(query):
    url = f"https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query={query}&format=json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

habitable_query = "SELECT TOP 30 pl_name, sy_dist * 3.26156 AS distance_light_years, pl_orblper, (pl_massj * 317.83) / POWER(pl_rade, 2) AS gravity, pl_rade FROM ps WHERE sy_dist IS NOT NULL AND pl_rade IS NOT NULL AND pl_orblper >= 365.25 * 0.8 AND pl_orblper <= 365.25 * 1.2 ORDER BY sy_dist;"
habitable_planets = get_exoplanet_data(habitable_query)

print("\n")

print(len(habitable_planets))

for planet in habitable_planets:
    print(f'{planet['pl_name']}: {planet['distance_light_years']} light years, Orbital period of {planet['pl_orblper']} days, gravity of {planet['gravity']}, radius of {planet['pl_rade']} Earth radii')

@app.route('/')
@app.route('/index')
def index():
    """Our default routes of '/' and '/index'

    Return: The content we want to display to a user
    """

    return render_template('index.html')


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
