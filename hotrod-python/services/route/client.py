import requests
import services.config.settings as config

class Route:
    def __init__(self, pickup, dropoff, eta):
        self.pickup = pickup
        self.dropoff = dropoff
        self.eta = eta

def compute_route(pickup, dropoff):
    uri = ('http://localhost:%d/route?pickup=%s&dropoff=%s'
                    % (config.ROUTE_PORT, pickup, dropoff) )
    return requests.get(uri)