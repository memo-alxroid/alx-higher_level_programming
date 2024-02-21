#!/usr/bin/python3
import json
""" Module that contains a function that returns the JSON representation of an object (string) """


def to_json_string(my_obj):
    """ Function that returns the JSON representation of an object (string) """
    return json.dumps(my_obj)
