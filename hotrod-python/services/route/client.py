import requests
import services.config.settings as config
import services.common.serializer as serializer

class Route:
    def __init__(self, pickup, dropoff, eta):
        self.pickup = pickup
        self.dropoff = dropoff
        self.eta = eta

def compute_route(pickup, dropoff):
    uri = ('http://localhost:%d/route?pickup=%s&dropoff=%s'
                    % (config.ROUTE_PORT, pickup, dropoff) )

    try:
        response = requests.get(uri)
        response_json = response.json()
        return serializer.json_to_obj(response_json)
    except Exception:
        return 'ERROR'