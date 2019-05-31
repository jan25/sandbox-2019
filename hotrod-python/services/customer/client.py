import requests
import config.settings as config

def get_customer(customer_id):
    uri = 'localhost:%d/customer?id=%s' % (config.CUSTOMER_PORT, customer_id)
    return requests.get(uri)