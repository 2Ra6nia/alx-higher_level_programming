#!/usr/bin/python3
"""Definig save_to_json_file function"""


import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation"""
    with open(filename, "w", encoding="utf-8"):
        return json.dumps(my_obj)
