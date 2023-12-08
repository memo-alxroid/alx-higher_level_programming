#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    for a_key, a_value in a_dictionary.items():
        if a_key == key:
            a_dictionary[a_key] = value
    a_dictionary[key] = value
    return a_dictionary
