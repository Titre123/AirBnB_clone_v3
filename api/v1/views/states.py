#!/usr/bin/python3
""" State objects API actiions """
from flask import Flask, jsonify, request, make_response, abort
from models import storage
from models.state import State
from datetime import datetime
from api.v1.views import app_views

@app_views.route('/states/', methods=['GET'])
def states():
    """ Retrieves the list of all State objects """
    x = storage.all("State")
    new_dict = []
    for key, value in x.items():
        new_dict.append(value.to_dict())
    return jsonify(new_dict)

@app_views.route('/states/<state_id>', methods=['GET'])
def stateId(state_id):
    """ Retrieves the list of all State objects """
    x = storage.get("State", state_id)
    new_dict = {}
    if x is None:
        abort(404)
    else:
        new_dict = x.to_dict()
    return jsonify(new_dict)

@app_views.route('/states/<state_id>', methods=['DELETE'])
def deleteStateId(state_id):
    """ Retrieves the list of all State objects """
    if request.method == 'DELETE':
        xo = storage.get("State", state_id)
        if xo is None:
            abort(404)
        xo.delete()
        storage.save()
        return jsonify({}), 200

@app_views.route('/states/', methods=['POST'])
def postState():
    """ Post new_state """
    if request.method == "POST":
        x = request.get_json()
        if not x:
            abort(400, 'Not a JSON')
        if not 'name' in x:
            abort(400, 'Missing Name')
        obj = State(**x)
        storage.new(obj)
        storage.save()
        return jsonify(obj.to_dict()), 201

@app_views.route('/states/<state_id>', methods=['PUT'])
def update(state_id):
    """ update """
    if request.method == "PUT":
        state = storage.get("State", state_id)
        x = request.get_json()
        if not x:
            abort(400, 'Not a JSON')
        for key, value in x.items():
            if key == "name":
                setattr(state, key, value)
        storage.save()
        return jsonify(y.to_dict()), 200
