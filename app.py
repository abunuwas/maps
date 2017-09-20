import json

from flask import Flask, render_template
import googlemaps


from config import geocode_api_key, places_api_key


app = Flask(__name__)
geocode = googlemaps.Client(geocode_api_key)
places = p = googlemaps.Client(places_api_key)


@app.route('/')
def index():
    center = {'lat': -25.363, 'lng': 131.044}
    return render_template('index.html', markers=json.dumps({'lat': -25.363, 'lng': 131.044}), center=center)


@app.route('/place/<string:name>')
def place(name):
    location = geocode.geocode(name)[0]['geometry']['location']
    return render_template('index.html', markers=location, center=location)


@app.route('/place/<string:name>/restaurants')
def restaurants(name):
    location = geocode.geocode(name)[0]['geometry']['location']
    outcome = p.places(location=location, query='restaurants')
    locations = [l['geometry']['location'] for l in outcome['results']]
    return render_template('index.html', markers=locations, center=location)


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)



