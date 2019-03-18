from flask import Flask, request
import os

from client import fibonacci

app = Flask(__name__)

POD_IP = os.environ.get('APP_POD_IP')

@app.route("/hi")
def hi():
    return "Hello, from " + str(POD_IP)

@app.route("/getfibonacci", methods=['GET'])
def getfibonacci():
    try:
        n = int(request.args.get('n'))
        return fibonacci.get_nth(n)
    except Exception as e:
        return ("ERROR in request handler: %s" % str(e))

@app.route("/health")
def health():
    return "all ok!"

if __name__ == "__main__":
    app.run("0.0.0.0", port=5000)