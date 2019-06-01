from flask import Flask

import services.config.settings as config

app = Flask(__name__)

@app.route('/find_nearest')
def find_nearest():
    return handle_find_nearest()

def handle_find_nearest():
    pass

def start_server():
    app.run(host='0.0.0.0', port=config.DRIVER_PORT, debug=True)

if __name__ == '__main__': start_server()