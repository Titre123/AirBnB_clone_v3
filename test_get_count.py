#!/usr/bin/python3
""" Test .get() and .count() methods
"""
from models import storage
from models.state import State

print("All objects: {}".format(storage.count()))
print("State objects: {}".format(storage.count()))

first_state_id = ''
print("First state: {}".format(storage.get(State, first_state_id)))
