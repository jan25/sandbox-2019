import requests
import services.config.settings as config

class Route:
    def __init__(self, pickup, dropoff, eta):
        self.pickup = pickup
        self.dropoff = dropoff
        self.eta = eta

def compute_route(driver, customer):
    uri = 'localhost:%d/compute_route' % config.ROUTE_PORT
    return requests.get(uri)