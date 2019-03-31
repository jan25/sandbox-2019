import requests
import os

FIBONACCI_SVC_NAME = os.environ.get('FIBONACCI_SVC_NAME')
FIBONACCI_HOST = 'http://%s' % FIBONACCI_SVC_NAME

def get_nth(n):
    try:
        return str(requests.get((FIBONACCI_HOST + '/fibonacci?n=%d') % n).content)
    except Exception as e:
        raise Exception(str(e))