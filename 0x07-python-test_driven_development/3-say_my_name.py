#!/usr/bin/python3
"""Module that prints a string with the first and last name"""


def say_my_name(first_name, last_name=""):
    """Prints a string with the first and last name
    Args:
        first_name (str): first name
        last_name (str): last name
    Returns: None
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    if any(char.isdigit() for char in first_name):
        raise TypeError("first_name must only contain letters")
    if any(char.isdigit() for char in last_name):
        raise TypeError("last_name must only contain letters")
    print("My name is {} {}".format(first_name, last_name))
