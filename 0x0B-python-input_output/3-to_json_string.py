#!/usr/bin/python3
""" Definig to_json_string function"""


import json


def to_json_string(my_obj):
    """ returns the JSON representation of an object"""
    return json.dumps(my_obj)
