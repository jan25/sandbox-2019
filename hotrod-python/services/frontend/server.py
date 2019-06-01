import os
from flask import Flask, send_from_directory, request

import services.config.settings as config
import services.customer.client as customer_client
import services.driver.client as driver_client
import services.route.client as route_client

# import opentracing
# from flask_opentracing import FlaskTracing
# from jaeger_client import Config

static_file_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'web_assets')
app = Flask(__name__)

# JAEGER_HOST = os.getenv('JAEGER_HOST', 'localhost')

# config = Config(config={'sampler': {'type': 'const', 'param': 1},
#                         'logging': True,
#                         'local_agent': {'reporting_host': JAEGER_HOST}
#                         },
#                 service_name="jaeger_opentracing_example")
# jaeger_tracer = config.initialize_tracer()
# tracing = FlaskTracing(jaeger_tracer, True, app)

@app.route("/")
def index():
    return send_from_directory(static_file_dir, 'index.html')

@app.route('/dispatch')
def dispatch():
    return handle_dispatch(request)

def handle_dispatch(request):
    customer_id = request.args.get('customer')
    customer = customer_client.get_customer(customer_id)

    drivers = driver_client.get_drivers()

    best_route, best_driver = -1, None
    for driver in drivers:
        route = route_client.compute_route(driver, customer)
        if best_route == -1 or route < best_route:
            best_driver = driver
    
    return best_driver

def start_server():
    app.run(host='0.0.0.0', port=config.FRONTEND_PORT, debug=True)

if __name__ == "__main__": start_server()