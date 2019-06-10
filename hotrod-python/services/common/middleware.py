import opentracing
from opentracing import tags
from opentracing.propagation import Format
import services.config.settings as config
from jaeger_client import Config
import requests

def before_request(request):
    tracer = opentracing.global_tracer()
    span = _before_request(request, opentracing.global_tracer())
    tracer.scope_manager.activate(span, True)

def _before_request(request, tracer):
    span_context = tracer.extract(
        format=Format.HTTP_HEADERS,
        carrier=request.headers,
    )
    print ('span_context', span_context)
    span = tracer.start_span(
        operation_name=request.path,
        child_of=span_context)
    span.set_tag('http.url', request.full_path)

    # remote_ip = request.remote_ip
    # if remote_ip:
    #     span.set_tag(tags.PEER_HOST_IPV4, remote_ip)

    # caller_name = request.caller_name
    # if caller_name:
    #     span.set_tag(tags.PEER_SERVICE, caller_name)

    # remote_port = request.remote_port
    # if remote_port:
    #     span.set_tag(tags.PEER_PORT, remote_port)

    return span

def after_request(response):
    tracer = opentracing.global_tracer()
    scope = tracer.scope_manager.active
    if scope: scope.close()

    return response


def init_tracer(service_name):
    JAEGER_HOST = config.JAEGER_HOST

    jaeger_config = Config(config={'sampler': {'type': 'const', 'param': 1},
                                'logging': 1,
                                'reporter_flush_interval': 100,
                                'local_agent': {
                                    'reporting_host': JAEGER_HOST
                                }
                            },
                        service_name=service_name)
    jaeger_config.initialize_tracer()

def http_get(uri, service_name='default-service'):
    # create and serialize a child span and use it as context manager
    current_span = opentracing.global_tracer().scope_manager.active.span
    span, headers = before_http_request(request_uri=uri,
                                        current_span=current_span,
                                        service_name=service_name)

    headers = headers or {}
    with span:
        print ('request.get(%s)' % uri)
        return requests.get(uri, headers=headers)

def before_http_request(request_uri, current_span, service_name):
    # op = request.operation
    # parent_span = current_span
    outbound_span = opentracing.global_tracer().start_span(
        operation_name=request_uri,
        child_of=current_span
    )

    outbound_span.set_tag('http.url', request_uri)
    # service_name = service_name
    # host, port = request.host_port
    if service_name:
        outbound_span.set_tag(tags.PEER_SERVICE, service_name)
    # if host:
    #     outbound_span.set_tag(tags.PEER_HOST_IPV4, host)
    # if port:
    #     outbound_span.set_tag(tags.PEER_PORT, port)

    http_header_carrier = {}
    opentracing.global_tracer().inject(
        span_context=outbound_span,
        format=Format.HTTP_HEADERS,
        carrier=http_header_carrier)

    headers = {}
    for key, value in http_header_carrier.items():
        headers[key] = value
        # request.add_header(key, value)


    print ('outbound_span', outbound_span)

    return outbound_span, headers