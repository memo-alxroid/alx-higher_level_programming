#!/usr/bin/python3
""" A module for input/output functions"""


def read_file(filename=""):
    """A function that reads a File"""

    with open(filename, encoding="utf-8") as file:
        for line in file:
            print(line, end="")
