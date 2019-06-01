from flask import Flask, request, jsonify
import random
import math

import services.config.settings as config
import services.common.serializer as serializer
from . import client

app = Flask(__name__)

@app.route('/route')
def route():
    return jsonify(handle_route(request))

def handle_route(request):
    pickup = request.args.get('pickup')
    dropoff = request.args.get('dropoff')
    return serializer.obj_to_json(compute_route(pickup, dropoff))

def compute_route(pickup, dropoff):
    eta = math.ceil(max(2, random.random()*3+5))
    return client.Route(pickup=pickup, dropoff=dropoff, eta=eta)

def start_server(debug):
    app.run(host='0.0.0.0', port=config.DRIVER_PORT, debug=debug)

if __name__ == '__main__': start_server(debug=True)