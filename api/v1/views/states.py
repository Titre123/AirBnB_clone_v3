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
    if request.methods == 'DELETE':
        x = storage.get("State", state_id)
        if x is None:
            abort(404)
        else:
            storage.delete(x)
            del x
            return jsonify({})

@app_views.route('/states/', methods=['POST'])
def postState():
    """ Post new_state """
    if request.methods == "POST":
        x = request.get_json()
        if not x:
            abort(400, 'Not a JSON')
        if not 'name' in x:
            abort(400, 'Missing Name')
        obj = State(**x)
        obj.save()
        return jsonify(obj.to_json()), 201

@app_views.route('/states/<state_id>', methods=['POST'])
def update(state_id):
    """ update """
    if request.methods == "PUT":
        y = storage.get("State", state_id).to_dict()
        x = request.get_json()
        if not x:
            abort(400, 'Not a JSON')
        for key, value in x:
            if key == "name":
                y[key] = value
                y["updated_at"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        return jsonify(y), 200
