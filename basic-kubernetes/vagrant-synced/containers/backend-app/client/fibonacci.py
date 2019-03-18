import requests

FIBONACCI_SVC_URL = 'http://fibonacci-service/fibonacci?n=%d'

def get_nth(n):
    try:
        return str(requests.get(FIBONACCI_SVC_URL % n).content)
    except Exception as e:
        raise Exception(str(e))