from flask import Flask, request

import services.config.settings as config

app = Flask(__name__)

@app.route('/compute_route')
def compute_route():
    return handle_compute_route(request)

def handle_compute_route(request):
    pickup = request.args.get('pickup')
    dropoff = request.args.get('dropoff')
    return actually_compute_route(pickup, dropoff)

def actually_compute_route(pickup, dropoff):
    pass

def start_server():
    app.run(host='0.0.0.0', port=config.DRIVER_PORT, debug=True)

if __name__ == '__main__': start_server()