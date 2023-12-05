#!/usr/bin/python3
'''Defines a student class.'''


class Student:
    '''A class that represents a student.'''
    def __init__(self, first_name, last_name, age):
        '''
        class initilizer function.

        args:
            first_name, last_name, age: attributes of the Student class
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''Retrieves a dictionary representation of a Student instance.

        If attrs is a list of strings, only attribute names contained
        in this list must be retrieved.
        Otherwise, all attributes must be retrieved.
        '''
        for i in attrs:
            if i == type(str):
                return self.first_name
            else:
                return self.__dict__
