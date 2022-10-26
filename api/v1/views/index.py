#!/usr/bin/python3
"""
index file
"""
from models import storage
from api.v1.views import app_views
from flask import jsonify, request

@app_views.route('/status', methods=['GET'])
def status():
    """ Return json status """
    if request.method == "GET":
        return jsonify({"status": "Ok"})

@app_views.route('/stats')
def stats():
    """ Create an endpoint that retrieves the number of each objects by type """
    classes = {"amenities": "Amenity", "cities": "City",
           "places": "Place", "reviews": "Review", "states": "State", "users": "User"}
    new_dict = {}
    for key, value in classes.items():
        x = storage.count(value)
        if key not in new_dict:
            new_dict[key] = x
    return jsonify(new_dict)
