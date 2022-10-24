#!/usr/bin/python3
from flask import Flask
from models import storage
import os
import sys
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)

@app.teardown_appcontext
def tearDown(self):
    """ TearDown the process """
    storage.close()

if __name__ == "__main__":
    app.run(host = os.getenv("HBNB_API_HOST"), port = os.getenv("HBNB_API_PORT"),
    threaded=True)
    sys.exit()
