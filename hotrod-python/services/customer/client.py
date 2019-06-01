import requests
import services.config.settings as config

class Customer:
    def __init__(self, id, name, location):
        self.id = id
        self.name = name
        self.location = location

def get_customer(customer_id):
    uri = 'localhost:%d/customer?id=%s' % (config.CUSTOMER_PORT, customer_id)
    response = requests.get(uri)
    return response
    