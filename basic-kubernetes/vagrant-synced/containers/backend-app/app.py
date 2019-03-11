from flask import Flask

app = Flask(__name__)

@app.route("/hi")
def hi():
    return "Hello, there!"

@app.route("/health")
def health():
    return "all ok!"

if __name__ == "__main__":
    app.run("0.0.0.0", port=5000)