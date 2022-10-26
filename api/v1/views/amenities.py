#!/usr/bin/python3
""" State objects API actiions """
from flask import Flask, jsonify, request, make_response, abort
from models import storage
from models.amenity import Amenities
from datetime import datetime
from api.v1.views import app_views

@app_views.route('/amenities/', methods=['GET'])
def amenities():
    """ Retrieves the list of all State objects """
    x = storage.all("Amenities")
    new_dict = []
    for key, value in x.items():
        new_dict.append(value.to_dict())
    return jsonify(new_dict)

@app_views.route('/amenities/<string:amenity_id>', methods=['GET'])
def amenityId(amenity_id):
    """ Retrieves the list of all State objects """
    x = storage.get("Amenities", amenity_id)
    new_dict = {}
    if x is None:
        abort(404)
    else:
        new_dict = x.to_dict()
    return jsonify(new_dict)

@app_views.route('/amenities/<string:amenity_id>', methods=['DELETE'])
def deleteAmenityId(state_id):
    """ Retrieves the list of all State objects """
    if request.method == 'DELETE':
        xo = storage.get("Amenities", amenity_id)
        if xo is None:
            abort(404)
        xo.delete()
        storage.save()
        return jsonify({}), 200

@app_views.route('/amenities/', methods=['POST'])
def postState():
    """ Post new_state """
    if request.method == "POST":
        x = request.get_json()
        if not x:
            abort(400, 'Not a JSON')
        if not 'name' in x:
            abort(400, 'Missing Name')
        obj = Amenity(**x)
        storage.new(obj)
        storage.save()
        return jsonify(obj.to_dict()), 201

@app_views.route('/amenities/<string:amenity_id>', methods=['PUT'])
def update(state_id):
    """ update """
    if request.method == "PUT":
        amenity = storage.get(Amenity, amenity_id)
        x = request.get_json()
        if not x:
            abort(400, 'Not a JSON')
        for key, value in x.items():
            if key == "name":
                setattr(amenity, key, value)
        storage.save()
        return jsonify(y.to_dict()), 200
