#!/usr/bin/python3
"""Module that contains Text indentation function"""


def text_indentation(text):
    """Prints a text with 2 new lines after
    each of these characters: ., ? and :
    Args:
        text (str): text to be printed
    Returns: None
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    text = text.replace('.', '.\n\n')
    text = text.replace('?', '?\n\n')
    text = text.replace(':', ':\n\n')

    for line in text.split("\n"):
        print(line.strip(), end="")
        if line.strip() != "" and line != text.split("\n")[-1]:
            print("\n\n", end="")
