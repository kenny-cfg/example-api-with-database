from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def ping():
    return jsonify({
        'message': 'pong'
    })


@app.route('/user', methods=['POST'])
def create_user():
    user_data = request.get_json()
    name = user_data['name']
    place_of_birth = user_data['placeOfBirth']
    return jsonify({
        'receivedName': name,
        'receivedPlaceOfBirth': place_of_birth
    })


if __name__ == '__main__':
    app.run(port=5000, debug=True)