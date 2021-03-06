import json
import time

from flask import Flask, render_template, send_from_directory
import googlemaps

from config import geocode_api_key, places_api_key


app = Flask(__name__, static_url_path='', static_folder='static', template_folder='templates')
geocode = googlemaps.Client(geocode_api_key)
p = googlemaps.Client(places_api_key)


#@app.route('/js/<path:path>')
#def send_js(path):
#    return send_from_directory('js', path)


@app.route('/')
def index():
    center = {'lat': -25.363, 'lng': 131.044}
    return render_template('index.html', markers=json.dumps({'lat': -25.363, 'lng': 131.044}), center=center)


@app.route('/place/<string:name>')
def place(name):
    location = [geocode.geocode(name)[0]['geometry']['location']]
    return render_template('index.html', markers=location, center=location)


@app.route('/place/<string:name>/restaurants')
def restaurants(name):
    location = geocode.geocode(name)[0]['geometry']['location']
    outcome = []
    _outcome = p.places(location=location, query='restaurants')
    outcome += _outcome['results']
    while 'next_page_token' in _outcome:
        time.sleep(1)
        retry = True
        while retry:
            print('retrying...')
            try:
                _outcome = p.places(location=location, query='restaurants', page_token=_outcome['next_page_token'])
            except googlemaps.exceptions.ApiError:
                time.sleep(1)
            else:
                retry = False
        outcome += _outcome['results']
        locations = [l['geometry']['location'] for l in outcome['results']]
    return render_template('index.html', markers=locations, center=location)


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)



