from flask import Flask, request, jsonify
import db
import config.settings as config

app = Flask(__name__)

@app.route('/customer')
def get_customer():
    customer_id = request.args.get('id')
    customer_obj = db.get_customer_by_id(customer_id)
    return jsonify(customer_obj)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=config.CUSTOMER_PORT, debug=True)