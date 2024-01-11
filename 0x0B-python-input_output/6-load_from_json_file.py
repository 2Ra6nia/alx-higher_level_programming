#!/usr/bin/python3
""" Defining load_from_json_file"""


import json


def load_from_json_file(filename):
    """ creates an Object from a “JSON file”"""
    with open(filenme, "r", encoding="utf-8") as f:
        return json.load(f)
