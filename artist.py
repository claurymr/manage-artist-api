from flask import Flask, jsonify
from flask_cors import CORS


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# list of artists
ARTISTS = [
    {
        'firstName': 'Samantha',
        'lastName': 'Moonwalker',
        'dateOfBirth': '05/05/1998',
        'contactInfo': {
            'street': '21 Moon Road, apt. 2',
            'state': 'Michigan',
            'city': 'Dust',
            'zipcode': 12122,
            'phone': 5555555555
        }
    },
    {
        'firstName': 'George',
        'lastName': 'Freezer',
        'dateOfBirth': '02/02/1995',
        'contactInfo': {
            'street': '6 Ski St.',
            'state': 'Michigan',
            'city': 'Snow',
            'zipcode': 12121,
            'phone': 5555555550
        }
    }
]

# sanity check route
@app.route('/artists', methods=['GET'])
def all_artists():
    return jsonify({
        'status': 'success',
        'artists': ARTISTS
        })


if __name__ == '__main__':
    app.run()