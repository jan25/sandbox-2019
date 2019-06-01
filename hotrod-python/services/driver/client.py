import requests
import services.config.settings as config
import services.common.serializer as serializer

class Driver:
    def __init__(self, driver_id, location):
        self.driver_id = driver_id
        self.location = location

def get_drivers(pickup):
    uri = 'http://localhost:%d/find_nearest?pickup=%s' % (config.DRIVER_PORT, pickup)
    response = requests.get(uri)
    try:
        drivers = response.json()
        for i in range(len(drivers)):
            drivers[i] = serializer.json_to_obj(drivers[i])
        return drivers
    except Exception:
        return 'ERROR'