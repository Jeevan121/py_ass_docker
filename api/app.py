import psutil
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy   dog'
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app, resources={r"/stats": {"origins": "http://0.0.0.0:5000"}})

@app.route('/stats')
def stats():
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent

    return jsonify({"ram": ram, "cpu": cpu})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
