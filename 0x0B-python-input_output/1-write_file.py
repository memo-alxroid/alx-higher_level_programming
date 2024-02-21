#!/usr/bin/python3
""" A module for input/output functions"""


def write_file(filename="", text=""):
    """A function that writes into a File """

    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
