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

    def to_json(self):
        """ Method that retrieves a dictionary representation
        of a Student instance """
        return self.__dict__
