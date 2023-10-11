#!/usr/bin/python3
"""
    contains load_from_json_file function
"""
import json


def load_from_json_file(filename):
    """ reads the JSON file,filename, and creates an object from it """
    with open(filename, "r", encoding="utf-8") as new_file:
        return json.load(new_file)
