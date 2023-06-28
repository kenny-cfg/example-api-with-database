from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def ping():
    return jsonify({
        'message': 'pong'
    })


if __name__ == '__main__':
    app.run(port=5000, debug=True)