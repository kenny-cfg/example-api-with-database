from flask import Flask, jsonify, request
from database_utils import create_user, get_all_users

app = Flask(__name__)


@app.route('/')
def ping():
    return jsonify({
        'message': 'pong'
    })


@app.route('/user', methods=['POST'])
def create_user_endpoint():
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


@app.route('/user/<int:id_of_user>', methods=['PUT'])
def update_user(id_of_user):
    print(id_of_user)
    return 'UPDATE -- TODO'


@app.route('/user')
def get_all_users_endpoint():
    users = get_all_users()
    return jsonify(users)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
