import requests
import services.config.settings as config
import services.common.serializer as serializer

class Customer:
    def __init__(self, id, name, location):
        self.id = id
        self.name = name
        self.location = location

def get_customer(customer_id):
    uri = 'http://localhost:%d/customer?id=%s' % (config.CUSTOMER_PORT, customer_id)
    response = requests.get(uri)
    try:
        response_json = response.json()
        return serializer.json_to_obj(response_json)
    except Exception:
        return 'ERROR'
    