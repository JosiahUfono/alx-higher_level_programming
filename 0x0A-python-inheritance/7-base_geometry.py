#!/usr/bin/python3
'''Defines a base geometry class BaseGeometry.'''


class BaseGeometry:
    '''Represents a the BaseGeometry class.'''

    def area(self):
        '''Not implemented.'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''Validate an argument as an integer.

        Arg:
            name: The name of the argument (str).
            value: The argument to be validated.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.'''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
