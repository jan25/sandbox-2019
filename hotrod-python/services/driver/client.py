import requests
import services.config.settings as config

class Driver:
    def __init__(self, driver_id, location):
        self.driver_id = driver_id
        self.location = location

def get_drivers():
    uri = 'localhost:%d/find_nearest' % config.DRIVER_PORT
    return requests.get(uri)