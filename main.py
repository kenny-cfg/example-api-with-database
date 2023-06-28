from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def ping():
    return jsonify({
        'message': 'pong'
    })


@app.route('/user', methods=['POST'])
def create_user():
    return 'CREATE USER'


if __name__ == '__main__':
    app.run(port=5000, debug=True)