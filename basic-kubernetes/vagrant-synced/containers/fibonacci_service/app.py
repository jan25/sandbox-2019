from flask import Flask, request
from fibonacci import api

app = Flask(__name__)

@app.route("/fibonacci", methods=['GET'])
def fibonacci():
    try:
        n = int(request.args.get('n'))
        return str(api.fibonacci(n))
    except Exception:
        return "ERROR: Invalid URL parameter. Example usage /fibonacci?n=13"

@app.route("/health", methods=['GET'])
def health():
    return "all ok!"

'''
For liveness probe
'''
@app.route("/healthz")
def healthz():
    return "I'm healthy, thanks :)"


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000)