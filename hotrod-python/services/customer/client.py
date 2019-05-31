import requests

CUSTOMER_PORT = 8081
def get_customer(customer_id):
    uri = 'localhost:%d/customer?id=%s' % (CUSTOMER_PORT, customer_id)
    return requests.get(uri)