from flask import Flask, jsonify, request

import services.common.serializer as serializer
import services.config.settings as config
from . import redis

app = Flask(__name__)

@app.route('/find_nearest')
def find_nearest():
    return jsonify(handle_find_nearest(request))

def handle_find_nearest(request):
    pickup = request.args.get('pickup')
    driver_ids = redis.find_drivers_ids(pickup=pickup)
    drivers = [redis.get_driver(_id) for _id in driver_ids]
    drivers = [serializer.obj_to_json(d) for d in drivers]
    return drivers

def start_server(debug):
    app.run(host='0.0.0.0', port=config.DRIVER_PORT, debug=debug)

if __name__ == '__main__': start_server(debug=True)