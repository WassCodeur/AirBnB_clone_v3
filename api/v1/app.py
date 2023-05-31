#!/usr/bin/python3
"""Status of my API"""


from api.v1.views import app_views
from flask import Flask, Blueprint, make_response, jsonify
from models import storage
import os
app = Flask(__name__)

app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_appcontext(code):
    storage.close()

@app.errorhandler
def page_not_found(404):
    return make_response(jsonify({'error': 'Not found'}))


if __name__ == '__main__':
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = os.getenv('HBNB_API_PORT', 5000)

    app.run(host=host, port=port, threaded=True)
