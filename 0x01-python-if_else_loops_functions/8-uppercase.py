#!/usr/bin/python3

def uppercase(str):
    upperString = ""
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            c = ord(c) - 32
            upperString += chr(c)
        else:
            upperString += chr(ord(c))
    print(upperString)
