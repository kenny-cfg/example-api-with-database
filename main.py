from flask import Flask, jsonify, request
from database_utils import create_user

app = Flask(__name__)


@app.route('/')
def ping():
    return jsonify({
        'message': 'pong'
    })


@app.route('/user', methods=['POST'])
def create_user():
    # Interpret (deserialize, marshall) the JSON into a Python map
    user_data = request.get_json()
    # Extract name from resulting map...
    name = user_data['name']
    # ...and place of birth
    place_of_birth = user_data['placeOfBirth']
    # Call the create_user method to actually dump the user into the DB
    create_user(name, place_of_birth)
    # Echo the results back to prove we've received it
    return jsonify({
        'receivedName': name,
        'receivedPlaceOfBirth': place_of_birth
    })


if __name__ == '__main__':
    app.run(port=5000, debug=True)