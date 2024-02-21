#!/usr/bin/python3
""" Module that contains a function that returns
the JSON representation of an object (string) """

import json


def from_json_string(my_str):
    """ Function that returns the JSON representation of an object (string) """
    return json.load(my_str)
