import os
from flask import Flask, send_from_directory

static_file_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'web_assets')
app = Flask(__name__)

@app.route("/")
def hello():
    return send_from_directory(static_file_dir, 'index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)