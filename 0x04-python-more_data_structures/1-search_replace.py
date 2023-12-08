#!/usr/bin/python3

def search_replace(my_list, search, replace):
    newList = []
    for item in my_list:
        newList.append(replace if item == search else item)
    return newList
