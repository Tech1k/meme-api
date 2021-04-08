from flask import Flask, jsonify
from api import MemeAPI

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/', methods = ['GET'])
def meme_api():
    result = MemeAPI()
    return jsonify(result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='80', threaded=True)
