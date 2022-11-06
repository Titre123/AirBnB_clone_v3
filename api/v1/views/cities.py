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


@app_views.route('/cities/<city_id>', methods=['DELETE'])
def deleteStateId(city_id):
    """ Retrieves the list of all State objects """
    if request.method == 'DELETE':
        xo = storage.get("City", city_id)
        if xo is None:
            abort(404)
        xo.delete()
        storage.save()
        return jsonify({}), 200


@app_views.route('/states/<state_id>/cities', methods=['POST'])
def postState(state_id):
    """ Post new_state """
    if request.method == "POST":
        y = storage.get("State", state_id)
        x = request.get_json()
        if y == None:
            abort(404)
        if not x:
            abort(400, 'Not a JSON')
        if 'name' not in x:
            abort(400, 'Missing Name')
        x['state_id'] = state_id
        obj = City(**x)
        storage.new(obj)
        storage.save()
        return jsonify(obj.to_dict()), 201


@app_views.route('/cities/<city_id>', methods=['PUT'])
def update(city_id):
    """ update """
    if request.method == "PUT":
        state = storage.get("City", city_id)
        x = request.get_json()
        if not x:
            abort(400, 'Not a JSON')
        for key, value in x.items():
            if key == "name":
                setattr(state, key, value)
        storage.save()
        return jsonify(state.to_dict()), 200
