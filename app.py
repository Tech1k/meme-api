from flask import Flask, jsonify
from api import ScrapMemes

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/')
def meme_api():
    result = ScrapMemes()
    return jsonify(result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='80', threaded=True)
