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

    def to_json(self):
        '''Retrieves a dictionary representation of a Student instance '''
        return self.__dict__