#!/usr/bin/python3
""" A module for input/output functions"""


def append_write(filename="", text=""):
    """A function that appends a string
         at the end of a text file into a File """

    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
