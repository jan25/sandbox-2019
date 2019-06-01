from flask import Flask, request, jsonify
from . import db
import services.config.settings as config
import services.common.serializer as serializer

app = Flask(__name__)

@app.route('/customer')
def get_customer():
    customer_id = request.args.get('id')
    customer_obj = db.get_customer_by_id(customer_id)
    return jsonify(serializer.obj_to_json(customer_obj))

def start_server(debug):
    app.run(host='0.0.0.0', port=config.CUSTOMER_PORT, debug=debug)

if __name__ == '__main__': start_server(True)