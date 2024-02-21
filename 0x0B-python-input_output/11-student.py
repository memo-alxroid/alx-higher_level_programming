#!/usr/bin/python3
""" Module that contains a class Student that defines a student by
 first_name, last_name and age """


class Student:
    """ Class that defines a student by first_name, last_name and age """
    def __init__(self, first_name, last_name, age):
        """ Constructor method for the Student class """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Method that retrieves a dictionary representation of a Student
        instance """
        if attrs is None:
            return self.__dict__
        else:
            new_dict = {}
            for key, value in self.__dict__.items():
                if key in attrs:
                    new_dict[key] = value
            return new_dict
    
    def reload_from_json(self, json):
        """ Method that replaces all attributes of the Student instance """
        for key, value in json.items():
            setattr(self, key, value)
