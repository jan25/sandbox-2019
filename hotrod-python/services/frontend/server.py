import os
import logging
import sys
from flask import Flask, send_from_directory, request, jsonify

import opentracing
from uwsgidecorators import postfork

import services.common.serializer as serializer
import services.config.settings as config
from . import eta

import services.common.middleware as middleware

static_file_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'web_assets')

app = Flask(__name__)

@postfork
def postfork():
    print ('postforking..')
    app.wsgi_app = middleware.FlaskMiddleware(service_name='frontend', app=app.wsgi_app)

def _log(this):
    print(this)
    sys.stdout.flush()

@app.route("/")
def index():
    with opentracing.global_tracer().start_span('index') as span:
        return send_from_directory(static_file_dir, 'index.html')

@app.route('/dispatch')
def dispatch():
    with opentracing.global_tracer().start_span('dispatch') as span:
        _log('/dispatch called')
        return middleware.RequestMiddleware.handle_request(request, handle_dispatch_and_jsonify)

def handle_dispatch_and_jsonify(request):
    return jsonify(handle_dispatch(request))

def handle_dispatch(request):
    customer_id = request.args.get('customer')
    return serializer.obj_to_json(eta.get_best_eta(customer_id))

def start_server(debug):
    app.run(host='0.0.0.0', port=config.FRONTEND_PORT, debug=debug)

if __name__ == "__main__": start_server(debug=True)