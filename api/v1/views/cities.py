#!/usr/bin/python3
""" Cities objects API actiions """
from flask import Flask, jsonify, request, make_response, abort
from models import storage
from models.city import City
from datetime import datetime
from api.v1.views import app_views


@app_views.route('/states/<state_id>/cities', methods=['GET'])
def cites(state_id):
    """ Retrieves the list of all State objects """
    x = storage.get("State", state_id)
    if x == None:
        abort(404)
    cities = x.cities
    new_dict = []
    for city in cities:
        new_dict.append(city.to_dict())
    return jsonify(new_dict)


@app_views.route('/cities/<city_id>', methods=['GET'])
def idcity(city_id):
    """ Retrieve vity based on id """
    x = storage.get("City", city_id)
    new_dict = {}
    if x is None:
        abort(404)
    else:
        new_dict = x.to_dict()
    return jsonify(new_dict)



