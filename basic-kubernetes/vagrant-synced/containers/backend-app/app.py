from flask import Flask
import os

app = Flask(__name__)

POD_IP = os.environ.get('APP_POD_IP')

@app.route("/hi")
def hi():
    return "Hello, from " + str(POD_IP)

@app.route("/health")
def health():
    return "all ok!"

if __name__ == "__main__":
    app.run("0.0.0.0", port=5000)