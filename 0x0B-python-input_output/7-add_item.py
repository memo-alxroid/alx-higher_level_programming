#!/usr/bin/python3
""" Module that contains  a script that adds all arguments
 to a Python list, and then save them to a file """

import sys


def main():
    """ Main function of the module """
    filename = "add_item.json"
    try:
        my_list = load_from_json_file(filename)
    except FileNotFoundError:
        my_list = []
    my_list.extend(sys.argv[1:])
    save_to_json_file(my_list, filename)


if __name__ == "__main__":
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    main()
