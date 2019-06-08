import os
from flask import Flask, send_from_directory, request, jsonify

import services.common.serializer as serializer
import services.config.settings as config
from . import eta

import opentracing
# from flask_opentracing import FlaskTracing
from jaeger_client import Config

static_file_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'web_assets')
app = Flask(__name__)

JAEGER_HOST = config.JAEGER_HOST

j_config = Config(config={'sampler': {'type': 'const', 'param': 1},
                        'logging': True,
                        'local_agent': {'reporting_host': JAEGER_HOST}
                        },
                service_name="frontend")
jaeger_tracer = j_config.initialize_tracer()
# tracing = FlaskTracing(jaeger_tracer, True, app)

@app.route("/")
def index():
    with jaeger_tracer.start_span('index') as span:
        return send_from_directory(static_file_dir, 'index.html')

@app.route('/dispatch')
def dispatch():
    with jaeger_tracer.start_span('dispatch') as span:
        return jsonify(handle_dispatch(request))

def handle_dispatch(request):
    customer_id = request.args.get('customer')
    return serializer.obj_to_json(eta.get_best_eta(customer_id))

def start_server(debug):
    app.run(host='0.0.0.0', port=config.FRONTEND_PORT, debug=debug)

if __name__ == "__main__": start_server(debug=True)