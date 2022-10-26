#!/usr/bin/python3
""" State objects API actiions """
from flask import Flask, jsonify, request, make_response, abort
from models import storage
from models.state import City
from datetime import datetime
from api.v1.views import app_views

@app_views.route('/states/<state_id>/cities', methods=['GET'])
def states(state_id):
    """ Retrieves the list of all State objects """
    allState_city = []
    if not storage.get(State, state_id):
        abort(404)
    for city in storage.all(City).values():
        if state_id == city.to_dict().get('state_id', None):
            allState_city.append(city.to_dict())
    return jsonify(allState_city)

@app_views.route('/cities/<city_id>', methods=['GET'])
def stateId(city_id):
    """ Retrieves the list of all State objects """
    x = storage.get("City", city_id)
    new_dict = {}
    if x is None:
        abort(404)
    else:
        new_dict = x.to_dict()
    return jsonify(new_dict)

@app_views.route('/city/<city_id>', methods=['DELETE'])
def deleteStateId(city_id):
    """ Retrieves the list of all State objects """
    if request.method == 'DELETE':
        xo = storage.get("City", city_id)
        if xo is None:
            abort(404)
        xo.delete()
        storage.save()
        return jsonify({}), 200

@app_views.route('/cities/', methods=['POST'])
def postState():
    """ Post new_state """
    if request.method == "POST":
        x = request.get_json()
        if not x:
            abort(400, 'Not a JSON')
        if not 'name' in x:
            abort(400, 'Missing Name')
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
        return jsonify(y.to_dict()), 200
