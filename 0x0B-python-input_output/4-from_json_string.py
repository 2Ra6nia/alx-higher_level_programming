#!/usr/bin/python3
""" Defining from_json_string finction"""


import json


def from_json_string(my_str):
    """retun an object represented by json"""
    return json.load(my_str)
